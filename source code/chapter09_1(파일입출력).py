# Chpater09-1
# 파일 읽기 및 쓰기

# 읽기 모드 : r
# 쓰기 모드 : w
# 추가 모드 : a
# 텍스트모드 : t
# 바이너리 모드 : b
# 상대 경로('../', ,/''), // 현재 위치부터 따져보겠다. 상대 경로가 주로 쓰인다.
# 절대 경로('D:\Django\example..')  // 현재 어디에 있던지 상관없이,,

# 파일 읽기(Read)
# 예제1
f = open('./resource/it_news.txt', 'r', encoding = 'UTF-8') # 'r'하면 디폴트가 text

# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)
# 반드시 close
f.close()
print()

# 예제2
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))
    print(len(c))
    print(type(c))
print()

# 예제3
# read() : 전체 읽기, read(10) : 10Byte만 읽어오기
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    c = f.read(20)
    print(c)
    print(iter(c))
    print(list(c))
    print(len(c))
    print(type(c))
    c = f.read(20)
    print(c)
    f.seek(0,0) # .seek 을 이용하면, 커서 위치를 처음으로 되돌릴 수 있다.
    c = f.read(20)
    print(c)
print()

# 예제4
# readline : 한 줄 씩 읽기

with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    line = f.readline()
    print(line)

# 예제5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print(type(cts))
    print(len(cts))
    for c in cts:
        print(c, end='')
print()

# 파일 쓰기(write)
# 예제1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

# 예제2
with open('./resource/contents1.txt', 'a') as f:
    f.write('I love python2\n')

# 예제3
# writelines : 리스트 -> 파일
with open('./resource/contents1.txt', 'a') as f:
    list = {'Orange\n', 'Apple\n'}
    f.writelines(list)

# 예제4
with open('./resource/contents1.txt', 'w') as f:
    print('Test Text Write', file = f)
    print('Test Text Write', file = f)
    print('Test Text Write', file = f)
