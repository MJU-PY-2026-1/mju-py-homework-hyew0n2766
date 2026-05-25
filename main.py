# 파일이름 : 3차 과제
# 작 성 자 : 60221856 김혜원

import random

print('===== ♛ 대학생 생존 서바이벌 ♛ =====')

# ===========================================
# 3차 전역 변수 영역
# ===========================================
# 인적 사항 입력 변수
character_name = ''
major = ''

word_count = 0
typing_score = 0
sleep_hours = 0.0

# 초기값
hp = 60.0
focus = 60.0
stress = 20.0
exp = 0
gold = 0
level = 1

# 오늘의 공부 기록 변수

study_hours = 0
study_subjects = []
study_times = []

# 공부 계획 완료 여부 확인 변수
completed_subjects = []
total_completed = 0

# 집중 공부 과목 수 계산 변수
focus_Record = 0

condition = ''
message = ''
warning = ''
bonus_message = ''

items = []
is_calculated = False

survival_records = []
record_headers = ['이름', '전공', '레벨', '총공부시간', '공부과목수', '완료과목수',
                  '집중공부과목수', '영단어수', '영타점수', '체력', '집중력',
                  '스트레스', '경험치', '골드', '보유보상']

# ===========================================
# 4차 추가 try-except 1: 정수 입력 예외 처리
# ===========================================

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('숫자(정수)로 입력해야 합니다. 다시 입력해주세요.')
            
# ===========================================
# 4차 추가 try-except 2: 실수 입력 예외 처리
# ===========================================
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('숫자(실수)로 입력해야 합니다. 다시 입력해주세요.')


# 3차 메뉴 출력 함수

def show_menu():
    print('\n==== 메인메뉴 ====')
    print('1. 인적 사항 입력')
    print('2. 공부 기록 입력')
    print('3. 공부 목록 정리')
    print('4. 공부 완료 여부 입력')
    print('5. 오늘의 생존 결과 조회')
    print('6. 현실 보상 상점 이용')
    print('7. 보상 사용하기')
    print('8. 일일미션')
    print('9. 누적 생존 기록 조회')
    print('10. 생존 기록 파일 저장')
    print('11. 저장 파일 확인')
    print('0. 종료')

# ===========================================
# 3차 추가 및 함수화
# ===========================================     
# 1. 인적 사항 입력

def input_personal_info():
    global character_name, major, word_count, typing_score, sleep_hours, is_calculated
    global hp, focus, stress, exp, gold, level
    global study_hours, total_completed, focus_Record
    global condition, message, warning, bonus_message
    global study_subjects,study_times,completed_subjects,items

    character_name = input('성함을 입력하세요: ')
    major = input('당신의 전공을 입력하세요: ')

    # 영어 단어 미니게임 변수
    word_count = 0
    typing_score = 0
    print('\n영단어 타자 미니게임을 통해 경험치를 획득하고 영어 실력을 성장시켜보세요!')

    # 수면 시간 입력
    sleep_hours = get_float('오늘의 수면 시간을 입력하세요: ')

    # 캐릭터 별 초기값
    hp = 60.0
    focus = 60.0
    stress = 20.0
    exp = 0
    gold = 0
    level = 1

    study_hours = 0
    total_completed = 0
    focus_Record = 0

    condition = ''
    message = ''
    warning = ''
    bonus_message = ''

    study_subjects = []
    study_times = []
    completed_subjects = []
    items = []


    is_calculated = False
    print('\n 인적 사항 등록을 성공하였습니다!')


# ===========================================
# 3차 추가 및 함수화
# =========================================== 
# 2. 오늘의 공부 기록
def input_study_record():
    global study_hours, is_calculated

    if character_name == '':
        print('\n1번 메뉴에서 인적 사항을 모두 입력한 후 다시 실행해주세요!')
        return

    print('\n오늘의 공부 기록')
    print("오늘의 공부가 모두 끝났다면 과목명에 '오늘치 공부 끝!'이라고 작성해주시길 바랍니다.")
        
    for i in range(20):
        subject = input(f'\n{i+1}번째 공부 과목: ')

        if subject == '오늘치 공부 끝!':
            print('오늘의 공부 기록 입력을 종료합니다.')
            break

        hours = get_int(f'{subject}을 공부한 시간을 입력하세요: ')

        if hours <= 0:
            print('잘못된 입력입니다. 다시 입력해주세요!')
            continue

        # 중복 과목 자동 합산
        if subject in study_subjects:
            subject_index = study_subjects.index(subject)
            study_times[subject_index] += hours
        else:
            study_subjects.append(subject)
            study_times.append(hours)

        study_hours += hours

    is_calculated = False
    print('정산을 시작합니다.')  


# ===========================================
# 3차 추가 및 함수화
# insert, remove, index 활용
# =========================================== 
# 3. 공부 목록 정리

def organize_study_list():
    global study_hours, is_calculated

    if character_name == '':
        print('\n1번 메뉴에서 인적 사항을 모두 입력한 후 다시 실행해주세요!')
        return

    if len(study_subjects) == 0:
        print('\n아직 입력된 기록이 없습니다! 공부 기록을 채워주시길 바랍니다.')
        return
    
    # 최우선 과목 맨 앞 배치
    priority_subject = input("\n오늘 가장 중요했던 과목을 입력하세요. 없다면 'Enter'를 누르세요.")

    if priority_subject in study_subjects:
        priority_index = study_subjects.index(priority_subject)
        priority_time = study_times[priority_index]

        study_subjects.remove(priority_subject)
        study_times.pop(priority_index)

        study_subjects.insert(0, priority_subject)
        study_times.insert(0, priority_time)
        
        print(f"'{priority_subject}'을(를) 최우선 과목으로 지정하였습니다.")

    # 잘못 입력한 과목 삭제
    remove_subject = input("\n잘못 입력한 과목이 있다면 입력하세요, 없다면 'Enter'를 누르세요.")

    if remove_subject in study_subjects:
        remove_index = study_subjects.index(remove_subject)
        remove_time = study_times[remove_index]

        study_subjects.remove(remove_subject)
        study_times.pop(remove_index)
        study_hours -=remove_time

        print(f"'{remove_subject}' 을(를) 삭제했습니다.")

    else:
        print('삭제할 과목이 존재하지 않거나 입력되지 않았습니다.')

    is_calculated = False

# ===========================================
# 3차 추가 및 함수화
# ===========================================           
# 4. 공부 완료 여부 입력
def check_completed_subjects():
    global completed_subjects, total_completed, is_calculated  
  
    if character_name == '':
        print('\n1번 메뉴에서 인적 사항을 모두 입력한 후 다시 실행해주세요!')
        return

    if len(study_subjects) == 0:
        print('\n아직 입력된 과목이 없습니다.')
        return
    
    completed_subjects = []
    total_completed = 0 
    
    print('\n각 과목의 완료 여부를 입력해주세요.')
    print('완료 시 yes, 아니라면 NO, 완료 여부 입력을 중단하려면 stop을 입력해주세요.')


    for subject in study_subjects:
        answer = input(f'{subject}의 하루 공부할당량을 채웠나요?')

        if answer == 'stop':
            print('완료 여부 확인을 중단합니다.')
            break

        if answer == 'NO' or answer == 'no':
            continue

        if answer == 'yes' or answer == 'YES':
            completed_subjects.append(subject)
            total_completed += 1
    
    is_calculated = False
    print('공부 완료 확인이 끝났습니다.')

# ===========================================
# 3차 추가: 매개변수 + return 사용 함수
# ===========================================
def count_focus_record(times):
    count = 0
    
    for study_time in times:
        if study_time >= 4:
            count += 1
    
    return count

def do_mission():
    global hp, focus, stress, exp, gold, level, word_count, typing_score, is_calculated
    
    if character_name == '':
        print('\n1번 메뉴에서 인적 사항을 모두 입력한 후 다시 실행해주세요!')
        return
    
    print('\n==== 일일 미션 🎮 ====')
    print('1. 1시간 휴식')
    print('2. 식사')
    print('3. 카페')
    print('4. 영단어 타자 미니게임')
    print('0. 미션 나가기')

    mission_choice = input('수행할 미션 번호를 입력하세요: ')

    if mission_choice == '1':
        hp += 5
        stress -= 10
        exp -= 3
        print('1시간 휴식을 통해 체력을 회복하고 스트레스를 완화시키세요.')
        
    elif mission_choice == '2':
        hp += 10
        print('식사를 통해 체력을 회복하세요!')

    elif mission_choice == '3':
        cafe_ticket = ''
       
        for item in items:
            if '카페' in item or '라떼' in item or '음료' in item or '티' in item:
                cafe_ticket = item
                break
            
        if cafe_ticket != '':
            items.remove(cafe_ticket)
            focus += 8
            stress -= 8

            update_latest_record() 

            print(f'{cafe_ticket}을(를) 사용했습니다!')
            print('음료 섭취를 통해 집중력을 증가시키고 스트레스를 감소시키세요!')
            
        else:
            print('사용 가능한 카페 이용권이 존재하지 않습니다...')
            print('상점을 방문해 카페 관련 보상을 구매해주세요!')    

    elif mission_choice == '4':
        print('\n==== 영단어 타자 미니게임 ====')
        print('총 30개의 파이썬 관련 영단어가 출제됩니다.')
        print('제시된 단어를 최대한 정확히 입력해주세요!')
        print('start!')

        words = ['while', 'for', 'range', 'start', 'stop', 'step', 'break', 'continue', 'loop',
                 'condition', 'count', 'print', 'input', 'menu', 'total', 'filter', 'sum', 'indexing',
                 'slicing', 'string', 'list', 'tuple', 'dictionary', 'set','index',
                 'append', 'split', 'method', 'database', 'challenge', 'final', 'structure', 'sequence',
                 'variable', 'integer', 'float', 'boolean', 'function', 'definition', 'call' , 'parameter',
                 'argument', 'return', 'local', 'global', 'scope', 'keyword', 'default', 'position', 'value',
                 'header', 'suite', 'execute', 'control', 'repeat', 'object', 'random', 'angle', 'distance', 'forward'
                 , 'left', 'right', 'turtle', 'graphics', 'library', 'import', 'shape', 'color', 'current',
                 'position', 'xcor', 'ycor', 'infinite', 'password', 'message', 'area', 'radius', 'calculate', 'processing',
                 'result', 'output', 'reusable', 'modular', 'flexible', 'indentation',
                 'syntax', 'range', 'step', 'start', 'stop', 'string', 'indexing', 'slicing',
                 'negative', 'positive', 'sequence', 'data', 'object', 'condition', 'True', 'False', 'elif',
                 'else', 'nested', 'challenge', 'mission', 'average', 'score', 'pass', 'fail', 'order',
                 'payment', 'discount', 'system', 'kiosk', 'smart', 'movie', 'cafe', 'POS', 'sales',
                 'review', 'repeat', 'iteration', 'execute', 'command', 'program', 'design', 'logic','module',
                 'interactive', 'visual', 'graphics', 'coordinate', 'movement', 'rotation', 'generate', 'randomize', 'accumulate',
                 'initialize', 'increment', 'decrement', 'validation', 'exception', 'process', 'operation', 'format',
                 'formatting', 'concatenate', 'multiply', 'divide', 'compare', 'retrieve', 'access', 'update', 'variable','definition',
                 'execution', 'declaration', 'reusable', 'maintainable'] 
        
        correct_count = 0
        total_mistake = 0
        total_length = 0

        for i in range(30):
            quiz_word = random.choice(words)

            print(f'\n{i+1}번째 단어: {quiz_word}')
            answer = input('입력: ')

            mistake = 0

            if len(quiz_word) < len(answer):
                short_length = len(quiz_word)
            else:
                short_length = len(answer)

            for j in range(short_length):
                if quiz_word[j] != answer[j]:
                    mistake += 1

            if len(quiz_word) > len(answer):
                mistake += len(quiz_word) - len(answer)
            elif len(quiz_word) < len(answer):
                mistake += len(answer) - len(quiz_word)

            total_mistake += mistake
            total_length += len(quiz_word)

            if answer == quiz_word:
                correct_count += 1     
            else:
                print(f'오답! 오타 개수: {mistake}개')

        if total_length > 0:
            accuracy = (total_length - total_mistake) / total_length * 100
        else:
            accuracy = 0
            print('잠이 부족하신가요? 숙면 후 타자 연습의 재진행을 권합니다.')

        if accuracy < 0:
           accuracy = 0

        word_count += correct_count
        typing_score += int(accuracy)

        exp += correct_count * 20
        gold += correct_count * 50
        stress += total_mistake

        print('\n==== 영단어 타자 미니게임 결과 ====')
        print(f'정답 개수 : 30개 중 {correct_count}개')
        print(f'총 오타 수 : 30 단어 작성 중 {total_mistake}개')
        print(f'정확도 : {accuracy:.1f}%')
        print(f'획득 영타 점수 : {int(accuracy)}점')
        print(f'획득 경험치 : {correct_count * 20}')
        print(f'획득 골드 : {correct_count * 50}골드')

        update_latest_record() 

    elif mission_choice == '0':
        print('일일미션 수행을 종료합니다')

    else:
        print('잘못된 메뉴 선택입니다!')

    level = exp // 100 + 1
    update_latest_record()

# 사용자 별 하루 생존 결과 저장 시스템
def make_result_row():
    if len(items) == 0:
        item_text = '없음'

    else:
        item_text = ''

        for i in range(len(items)):
            item_text += items[i]

            if i != len(items) - 1:
                item_text += '/' 

    row = [character_name, major, level, study_hours, len(study_subjects),
           total_completed, focus_Record, word_count, typing_score, hp, focus, stress, exp, gold, item_text]       

    return row

def update_latest_record():
    if len(survival_records) > 0 and is_calculated == True:
        survival_records[-1] = make_result_row()

# ===========================================
# 3차 추가 및 함수화 + return 사용 함수
# ===========================================
def calculate_status():
    global hp, focus, stress, exp, gold, level
    global condition, message, warning, bonus_message, focus_Record, is_calculated

    if character_name == '':
        print('\n1번 메뉴에서 인적 사항을 모두 입력한 후 다시 실행해주세요!')
        return

    if is_calculated == True:
        return exp, gold

    focus_Record = count_focus_record(study_times)

    # 능력치 계산
    exp += study_hours * 15
    gold += focus_Record * 1000
    focus -= study_hours * 3
    stress += study_hours * 6

    hp += sleep_hours * 5
    focus += sleep_hours * 4
    stress -= sleep_hours * 3

    exp += word_count * 2
    gold += (word_count%10)*1000

    exp += total_completed * 10
    gold += total_completed * 1000 

    if typing_score >= 100:
        exp += 5    

    # 캐릭터 상태 판정
    if stress >= 85:
        condition = '스트레스 누적, 지금 당장 휴식을 권고합니다.'
    elif stress >= 75:
        condition = '피로가 누적되었습니다. 금일 8시간 이상의 수면 시간 확보를 추천합니다.'
    elif stress >= 20:
        condition = '현재의 컨디션을 유지하면서 목표 달성을 위한 노력을 하시길 응원합니다.'
    else:
        condition = '최상의 컨디션입니다. 공부 목표를 좀 더 향상시켜도 좋을 것 같습니다.'

    # 추가 평가
    if study_hours >= 8 and word_count >= 50:
        exp += 100
        gold += 2000
        message = '서바이벌의 상위권을 노려봐도 좋은 것 같습니다.'
    else:
        message = '생존하는 그 날까지 좀 더 분발하시길 바랍니다.'

    # 레벨 
    if exp >= 100:
        level = exp // 100 + 1
    else:
        level = 1   

    # 공부 외 영역 평가
    if sleep_hours <= 5:
        if stress > 80:
            warning = '수면 부족과 높은 스트레스로 휴식이 필요합니다.'
        else:
            warning = '수면 시간이 부족합니다. 수면 시간을 확보하세요.'
    else:
        warning = '상태가 안정적입니다.'  

    # 공부 외 평가 2
    if hp >= 80 or focus > 80:
        bonus_message = '오늘의 컨디션이 아주 좋습니다.'
    else:
        bonus_message = '컨디션 관리를 추천합니다.' 
    
    is_calculated = True

    survival_records.append(make_result_row())

    return exp, gold

# ===========================================
# 3차 추가 및 함수화
# ===========================================
# 결과 출력
def print_result():
    if character_name == '':
        print('\n인적 사항 입력이 완료되지 않았습니다. 1번 메뉴 먼저 실행해주세요.')
        return
    
    calculate_status()

    print('\n===== 🔥오늘의 생존 결과🔥 =====') 
    print(f'이름: {character_name}')
    print(f'전공: {major}')
    print(f'레벨: Lv.{level}')

    print('\n~~~~~ 오늘의 공부 기록 ~~~~~')

    if study_hours > 0:

        for i in range(len(study_subjects)):
            subject = study_subjects[i]
            time = study_times[i]

            ratio = time / study_hours * 100
            print(f'{subject}: {time}hour ({ratio:.1f}%)')

    else:
        print('아직 입력된 공부 기록이 없습니다!')
        print('입력 후 다시 시도해주세요.')

    print(f'\n총 공부 시간: {study_hours}hour')
    print(f'공부 과목 수: {len(study_subjects)}개')
    print(f'집중 공부 과목 수: {focus_Record}개')

    if len(study_times) >0:
        print(f'가장 오래 공부한 시간: {max(study_times)}hour')
        
    print(f'\n 오늘 암기한 영어 단어 수: {word_count}개')
    print(f'오늘의 영타 점수: {typing_score}점')

    print('\n===== 공부 목록 =====')
    print(f'전체 공부 목록: {study_subjects}')
    print(f'오늘치 할당량 채운 과목: {total_completed}개')
    print(f'할당치 채운 과목 목록: {completed_subjects}')
    print(f'보유 보상 목록: {items}')

    print('\n===== 최종 능력치⚔️ =====')
    print(f'체력: {hp:.1f}')
    print(f'집중력: {focus:.1f}')
    print(f'스트레스: {stress:.1f}')
    print(f'경험치(EXP): {exp}')
    print(f'골드: {gold}')

    print('\n===== 상태 메세지 ======')
    print(f'현재 상태: {condition}')
    print(f'격려의 말: {message}')
    print(f'경고: {warning}')
    print(f'컨디션: {bonus_message}')

    print('\n오늘도 시험기간에서 살아남았습니다. 고생하셨습니다.')

# ===========================================
# 3차 추가
# ===========================================
# 상점

def use_shop():
    global gold

    if character_name == '':
        print('\n1번 메뉴에서 인적 사항을 모두 입력한 후 다시 실행해주세요!')
        return

    if is_calculated == False:
        print('\n오늘의 정산이 아직 완료되지 않았습니다!')
        print('5번 메뉴에서 오늘의 생존 결과를 먼저 조회한 후 상점을 이용해주세요.')
        return

    print('\n==== 현실 보상 상점 🛒 ====')  
    print(f'현재 보유 골드: {gold}')
    print('1. 카페 그라지에 아이스티 구매권: 2,500골드')
    print('2. 편의점 초콜릿 구매권: 2,000골드')
    print('3. 일일 자유시간권: 50,000골드')
    print('4. 랜덤 보상 룰렛 🎰 ')
    print('0. 상점 나가기')

    shop_choice = input('구매할 메뉴 번호를 입력하세요!')

    if shop_choice == '1':
        if gold >= 2500:
            gold -= 2500
            items.append('카페 그라지에 아이스티 구매권')
            print('카페 그라지에 아이스티 구매권을 획득했습니다.')

        else:
            print('골드가 부족합니다.')

    elif shop_choice == '2':
        if gold >= 2000:
            gold -= 2000
            items.append('편의점 초콜릿 구매권')
            print('편의점 초콜릿 구매권을 획득했습니다.')

        else:
            print('골드가 부족합니다.')  

    elif shop_choice == '3':
        if gold >= 50000:
            gold -= 50000
            items.append('일일 자유시간권')
            print('일일 자유시간권을 획득했습니다.')

        else:
            print('골드가 부족합니다.') 

    elif shop_choice == '4':
        print('==== 랜덤 보상 룰렛 🎰 ====')
        random_item = input('구매하고 싶은 품목 입력(Ex. 카페 1회 이용권, 배민 이용권, 1시간 여가시간 이용권 ):')

        if '밥' in random_item or '파스타' in random_item or '쿠팡' in random_item or '배민' in random_item or '치킨' in random_item or '떡볶이' in random_item :
            min_price = 8000
            max_price = 30000

        elif '영화' in random_item or '노래방' in random_item or '게임' in random_item or '자유' in random_item or '여가' in random_item or '만화카페' in random_item :
            min_price = 5000
            max_price = 50000  

        elif '티' in random_item or '라떼' in random_item or '스무디' in random_item or '쉐이크' in random_item or '과자' in random_item or '초코' in random_item or '초콜릿' in random_item or '음료' in random_item or '카페' in random_item or '편의점' in random_item:  
            min_price = 500
            max_price = 7000              
            
        else:
            min_price = 500
            max_price = 100000                            

        random_price = random.randint(min_price, max_price)

        print(f'{random_item}을(를) {random_price}골드로 구매하실 수 있습니다!')
        buy_choice = input('구매하시겠습니까? yes/no: ')

        if buy_choice == 'yes' or buy_choice == 'YES':
            if gold >= random_price:
                gold -= random_price
                items.append(random_item)
                print(f'{random_item} 구매권을 획득했습니다.')
            else:
                print('골드가 부족하여 구매에 실패하였습니다! 다음 기회에..')
        else:
            print('구매를 선택하지 않으셨습니다!')
            print(f'{random_item} 구매권이 사라집니다.')
            print('다음 기회에..')                       

    elif shop_choice == '0':
        print('상점을 나갑니다. 다음 방문을 기다리겠습니다!')

    else:
        print('잘못된 메뉴 선택입니다. 없는 메뉴일 경우엔 4번 랜덤 선택을,')
        print('상점을 나가시고 싶을 경우엔 0번을 눌러주세요.')    

# ===========================================
# 3차 추가
# ===========================================
# 보상 사용
def use_reward():

    if character_name == '':
        print('\n1번 메뉴에서 인적 사항을 모두 입력한 후 다시 실행해주세요!')
        return

    if len(items) == 0:
        print('\n아직 사용할 수 있는 보상이 없습니다.')
        print('상점 방문 후 다시 이용해주세요.')
        return
    
    print('\n ==== 보유 보상 목록 🎁 ====')
    
    for item in items:
        print(f'- {item}')

    reward = input('사용할 보상 이름을 입력해주세요!')

    if reward in items:
        if '티' in reward or '라떼' in reward or '스무디' in reward or '쉐이크' in reward or '음료' in reward or '카페' in reward :
            print('카페 관련 보상은 8번 일일 미션 수행의 카페 이용에서만 사용 가능합니다!')
            print('메인 메뉴에서 일일미션을 선택해주세요!')

        else:    
            items.remove(reward)
            update_latest_record()
            print(f'{reward}을(를) 사용하셨습니다!')
            print('즐거운 시간 되시길 바랍니다.')
    else:
        print('해당 보상을 보유하고 있지 않습니다.')
        print('상점 방문을 추천드립니다.')

# ===========================================
# 4차 추가 이중리스트 출력
# ===========================================
# 9. 누적 생존 기록 조회
def print_survival_records():
    if len(survival_records) == 0:
        print('\n아직 누적된 생존 기록이 없습니다..!')
        return
    
    print('\n==== 누적 생존 기록 ⚔️ ====')

    for header in record_headers:
        print(f'{header}', end = '\t')
    print()

    for row in survival_records:
        for data in row:
            print(f'{data}', end ='\t')        
        print()

# ===========================================
# 4차 추가 파일 저장 write
# ===========================================
# 10. 생존 기록 파일 저장
def save_records_to_file():
    if len(survival_records) == 0:
        print('\n저장할 생존 기록이 없습니다.')
        return
    
    try:
        with open('survival_records.txt', 'w', encoding = 'utf-8') as file:
            for i in range(len(record_headers)):
                file.write(str(record_headers[i]))
                if i < len(record_headers) - 1:
                    file.write(',')
            file.write('\n')

            for row in survival_records:
                for i in range(len(row)):
                    file.write(str(row[i]))
                    if i < len(row) - 1:
                        file.write(',')

                file.write('\n')

        print('\nsurvival_records.txt 파일 저장이 완료되었습니다!')

    except OSError:
        print('파일 저장 중 오류가 발생했습니다!') 

# ===============================================
# 4차 추가 파일 확인 및 FileNotFoundError 예외 처리
# ===============================================
# 11. 저장 파일 확인
def read_saved_file():
    try:
        with open('survival_records.txt', 'r', encoding = 'utf-8') as file:
            print('\n==== 저장된 파일 내용 ====')
            lines = file.readlines()

            for line in lines:
                print(line, end = '')

    except FileNotFoundError:
        print('\n저장된 파일이 없습니다.')
        print(' 먼저 10번 메뉴를 실행해 파일을 저장해주세요!')

# main logic
# while True + break

while True:

    show_menu()
    choice = input('메뉴를 선택하세요: ')

    if choice == '1':
        input_personal_info()

    elif choice == '2':
        input_study_record()

    elif choice == '3':
        organize_study_list()

    elif choice == '4':
        check_completed_subjects()        

    elif choice == '5':
        print_result()

    elif choice == '6':
        use_shop()

    elif choice == '7':
        use_reward()

    elif choice == '8':
        do_mission()

    elif choice == '9':
        print_survival_records()

    elif choice == '10':
        save_records_to_file()

    elif choice == '11':
        read_saved_file()


    elif choice == '0':
        print('\n프로그램 종료!')
        break
    
    else:
        print('잘못된 입력입니다. 다시 입력해주세요.')      