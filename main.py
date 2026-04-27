# 파일이름 : 2차 과제
# 작 성 자 : 60221856 김혜원

print('===== ♛ 대학생 생존 서바이벌 ♛ =====')

# 인적 사항 입력
character_name = input('성함을 입력하세요: ')
major = input('당신의 전공을 입력하세요: ')

# 영어 관련 입력 - 단순 구현
word_count = int(input('오늘 외운 영어 단어 수를 입력하세요: '))
typing_score = int(input('영어 타자 점수를 입력하세요: '))

# 수면 시간 입력
sleep_hours = float(input('오늘의 수면 시간을 입력하세요: '))

# 초기값
hp = 60.0
focus = 60.0
stress = 20.0
exp = 0
gold = 0

# 오늘의 공부 기록

study_hours = 0
study_subjects = []
study_times = []

print('\n오늘의 공부 기록')
print("오늘의 공부가 모두 끝났다면 과목명에 '오늘치 공부 끝!'이라고 작성해주시길 바랍니다.")
      
for i in range(20):
    subject = input(f'\n{i+1}번째 공부 과목: ')

    if subject == '오늘치 공부 끝!':
        print('오늘의 공부 기록 입력을 종료합니다.')
        print('정산을 시작합니다.')
        break

    hours = int(input(f'{subject}을 공부한 시간을 입력하세요.')) 

    if hours < 0:
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

# 최우선 과목 맨 앞 배치
priority_subject = input("\n오늘 가장 중요했던 과목을 입력하세요. 없다면 'Enter'를 누르세요.")

if priority_subject in study_subjects:
    priority_index = study_subjects.index(priority_subject)
    priority_time = study_times[priority_index]

    study_subjects.remove(priority_subject)
    study_times.remove(priority_time)

    study_subjects.insert(0, priority_subject)
    study_times.insert(0, priority_time)
    
# 잘못 입력한 과목 삭제
remove_subject = input("\n잘못 입력한 과목이 있다면 입력하세요, 없다면 'Enter'를 누르세요.")

if remove_subject in study_subjects:
    remove_index = study_subjects.index(remove_subject)
    remove_time = study_times[remove_index]

    study_subjects.remove(remove_subject)
    study_times.remove(remove_time)
    study_hours -=remove_time

# 공부 계획 완료 여부 확인
completed_subjects = []
total_completed = 0

print('\n각 과목의 완료 여부를 입력해주세요.')
print('완료 시 yes, 아니라면 NO, 완료 여부 입력을 중단하려면 stop을 입력해주세요.')

for subject in study_subjects:
    answer = input(f'{subject}의 하루 공부할당량을 채웠나요?')

    if answer == 'stop':
        print('완료 여부 입력을 중단합니다.')
        break
    if answer == 'NO' or answer == 'no':
       continue

    if answer == 'yes' or answer == 'YES':
        completed_subjects.append(subject)
        total_completed += 1

# 집중 공부 과목 수 계산
focus_Record = 0

for study_time in study_times:
    if study_time >= 4:
        focus_Record += 1

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

# 결과 출력
print('\n===== 🔥오늘의 생존 결과🔥 =====') 
print(f'이름: {character_name}')
print(f'전공: {major}')

print('\n~~~~~ 오늘의 공부 기록 ~~~~~')

for i in range(len(study_subjects)):
    subject = study_subjects[i]
    time = study_times[i]

    ratio = time / study_hours * 100
    print(f'{subject}: {time}hour ({ratio:.1f}%)')

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







   