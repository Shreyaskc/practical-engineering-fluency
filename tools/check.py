from pathlib import Path
import subprocess,sys,json,zipfile,tempfile
r=Path(__file__).resolve().parents[1]
lessons=json.loads((r/'lessons.json').read_text());assert [l['id'] for l in lessons]==list(range(1,13))
for group,success in [('labs',False),('references',True)]:
 for p in sorted((r/group).iterdir()):
  out=subprocess.run([sys.executable,'-m','unittest','-v'],cwd=p,capture_output=True,text=True)
  assert (out.returncode==0)==success, out.stdout+out.stderr
  print(group,p.name,'PASS' if success else 'EXPECTED FAILURE')
for p in (r/'downloads').glob('*.zip'):
 with zipfile.ZipFile(p) as z:
  assert all(not n.startswith('/') and '..' not in Path(n).parts for n in z.namelist())
  assert z.testzip() is None
print('Lesson sequence and ZIP integrity OK')
