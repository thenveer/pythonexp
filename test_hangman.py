from hangman import get_secret_word, hide_word , game ,continue_or_exit ,get_status
 
def test_secret_word_no_punctuation():
    with open("/tmp/words.txt","w") as f:
        for i in ["word'one", "word_two", "wordthree"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == "wordthree"
 
def test_secret_word_atleast_five():
    with open("/tmp/words.txt","w") as f:
        for i in ["wo", "wor", "word", "bigword"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == "bigword"
 
def test_secret_word_lowercase():
    with open("/tmp/words.txt","w") as f:
        for i in ["Wording", "wOrding", "WORDING", "wording"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == "wording"
 
def test_secret_word_no_repeat():
    with open("/tmp/words.txt","w") as f:
        for i in ["disaster","recall","advise","national","infrastructure","shots","fired", "federation", "duress"]:
            f.write(i+"\n")
    l = []
    for i in range(3):
        l.append(get_secret_word('/tmp/words.txt'))
    assert len(set(l)) == 3


def test_hide_word_empty():
    s="bigger"
    guess=[]
    assert hide_word(s,guess) == "______"

def test_hide_word_correct_letter():
      s="bigger"
      guess=['g']
      assert hide_word(s,guess) == "__gg__"

def test_full_corect_word():
     s="bigger"
     guess=['b','g','i','r','e']
     assert hide_word(s,guess) == "bigger"
     

def test_wrong_word_comes():
    s="bigger"
    guess=['z']
    assert hide_word(s,guess) == "______"
    
def test_when_guessing_word():
    s="bigger"
    correct_word=[]
    worng_word=[]
    guess_word=["i",'g']

    assert game(s,correct_word,worng_word,guess_word)== ("_igg__",['i','g'],[])

def test_when_guessing_correct_word():
    s="bigger"
    correct_word=['g']
    worng_word=[]
    guess_word=['i','g']

    assert game(s,correct_word,worng_word,guess_word)== ("_igg__",['g','i'],[])

def test_when_wrong_word():
    s="bigger"
    correct_word=[]
    worng_word=['k']
    guess_word=["i",'g']

    assert game(s,correct_word,worng_word,guess_word)== ("_igg__",['i','g'],['k'])

def test_when_wrong_word_repect():
    s="bigger"
    correct_word=[]
    worng_word=['k']
    guess_word=["i",'g','k']

    assert game(s,correct_word,worng_word,guess_word)== ("_igg__",['i','g'],['k'])

def test_when_guessing_wrong_word():
    s="zigger"
    correct_word=[]
    worng_word=['k']
    guess_word=["i",'g','l']

    assert game(s,correct_word,worng_word,guess_word)== ("_igg__",['i','g'],['k','l'])

def test_continue_or_exist_wrong_guess():
    s="bigger"
    correct_word=['g']
    worng_word=['k']
    guess_word=['z']
    assert continue_or_exit(s,correct_word,worng_word,guess_word)==("__gg__",['g'],['k','z'],1)

def test_continue_or_exist_correct_guess():
    s="biggel"
    correct_word=['g']
    worng_word=['k']
    guess_word=['b']
    assert continue_or_exit(s,correct_word,worng_word,guess_word)==("b_gg__",['g','b'],['k'],1)

    
def test_continue_or_exist_wrong_gues_get_exit():
    s="aigger"
    correct_word=['g']
    worng_word=['k']
    guess_word=['z','p','l','q','j','y']
    assert continue_or_exit(s,correct_word,worng_word,guess_word)==("__gg__",['g'],['k','z','p','l','q','j','y'],2)


def test_continue_or_exist_correct_full_guess():
    s="battlement"
    correct_word=[]
    worng_word=[]
    guess_word=['b','a','t','l','e','m','n']
    assert continue_or_exit(s,correct_word,worng_word,guess_word)==("battlement",['b','a','t','l','e','m','n'],[],3)
     
def test_get_status():
    s="bigger"
    correct_word=['g']
    worng_word=[]
    guess_word=['i','k','z']
    assert get_status(s,correct_word,worng_word,guess_word)=="""
guess = gikz
turn left =5 
"""   
