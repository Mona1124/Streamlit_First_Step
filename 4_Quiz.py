import streamlit as st

st.title('Quiz')
st.markdown('간단한 퀴즈를 풀어보아요 :sunglasses:')

b = st.radio('**1. 다음 중 \'현대자동차\'의 비전으로 옳은 것은?**', ['대기중 :thought_balloon:', '똥', '인류애', '똥 먹기'])
if b == '인류애':
    st.write(':red[정답입니다.] :kissing_heart:')
else:
    if b == '대기중 :thought_balloon:':
        st.write('가장 지루한 중학교는? 로딩중 	:smirk:')
    else: st.write('다시 도전하세요. :sweat:')


c = st.radio('**2. 다음 중 \'현대자동차\'의 2010년대 차종으로 옳지 않은 것은?**', ['대기중 :thought_balloon:', '벨로스터', '아이오닉', '고죠사토루 K77'])
if c == '고죠사토루 K77':
    st.write(':red[정답입니다.] :kissing_heart:')
else:
    if c == '대기중 :thought_balloon:':
        st.write('가장 지루한 중학교는? 로딩중 	:smirk:')
    else: st.write('다시 도전하세요. :sweat:')




d = st.radio('**3. 다음 중 가장 잘생긴 사람은?**', ['대기중 :thought_balloon:','하정훈 교수님', '차은우', '서강준'])
if d == '하정훈 교수님':
    st.write(':red[정답입니다.] :kissing_heart:')
else:
    if d == '대기중 :thought_balloon:':
        st.write('가장 지루한 중학교는? 로딩중 	:smirk:')
    else: st.write('다시 도전하세요. :sweat:')

a = st.checkbox("퀴즈를 다 풀고 체크해주세요 :bell:")
if a == True:
    st.write(":red[모든 소개가 끝났습니다. 감사합니다. Have a good day] :sunglasses:")