#9-1
def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())


#9.2
def get_odds():
    for num in range(1, 10):
        if num % 2 == 1:
            yield num
            num = num + 1

cnts = 0
odds = get_odds()
for i in odds:
    cnts += 1
    if cnts == 3:
        print(i)


#9.3
def test(new):
    def new_test(*args, **kwargs):
        print('start')
        result = new(*args, **kwargs)
        print('end')
        return result
    return new_test
@test
def bad(a, b):
    return a - b
bad(5, 3)



#9.4
class OopsException(Exception):
    pass
try:
    raise OopsException('aaaaa')
except OopsException as aaa:
    print('Caight an Oops')




#심심한 연습문제

groups = {
    '빅뱅': ['GD', '태양', '탑', '대성', '승리'],
    '마마무': ['문별', '솔라', '휘인', '화사']
}
print(groups.keys())
for k, v in groups.items():
    print(f'{k}의 멤버')
    for i in v:
        if i != '승리':
            print(i)
