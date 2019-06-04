import fileInfo

# the example file contains 7 ies 78 chars and 8 lines as follows:
# einie 
# menie
# mainie 
# mo
# got a ie
# tieger by 
# the toie
# total of 7 ie repetitions

def test_fileinfo():
    x = fileInfo.getlinenumbers("test.txt","ie")
    assert x[0] == 8
    assert x[1] == 78
    assert x[2] == 7