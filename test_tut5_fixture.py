from tut5 import save_dict
import os
import json
def test_save_dict(tmpdir):
    filepath=os.path.join(tmpdir,"test.json")
    d={"a":1,"b":2}
    save_dict(d,filepath)
    assert json.load(open(filepath,'r'))==d

#or
#if you want to to check the the function is printing something 
def test_save_dict_1(tmpdir,capsys):
    filepath=os.path.join(tmpdir,"test.json")
    d={"a":1,"b":2}
    save_dict(d,filepath)
    assert capsys.readouterr().out=="saved\n"#bcoz print saatement prints next line also
