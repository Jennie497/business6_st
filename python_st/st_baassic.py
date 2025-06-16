import streamlit as st

st.title('관심사항, 관심분야, 관심기업에 대한 소개💻📝')

st.header('관심사항 : 최근 경영트렌드, 관심분야:  마케팅, 관심기업 : cg제일제당')


st.markdown(
'''


    1. ***관심있는 마케팅 분야***

    
    1-1 **마케팅 분야 관심도**

    1-2 **마케팅 분야별 정의** 

    1-3 **신제품 개발 및 시장 분석**

  2. ***관심있는 최신 경영 트렌드***


    2-1 **ESG 경영과 소비자 인식**

    2-2 **광고, sns 전략 여기다가 영상**

    2-3 **식품 산업의 변화**

  3. ***관심있는 기업, cj 제일제당***

  
    3-1 **브랜드 파워와 혁신의 공존**

    3-2 **CJ제일제당 연도별 마케팅 비용**

    3-3 **CJ제일제당 다양한 사업 포트폴리오**

    3-4 **CJ제일제당 포트폴리오 실적 변화**


  4. ***느낀점***
'''
)

st.subheader('1. 관심있는 마케팅 분야')

import pandas as pd

st.write('*1-1 마케팅 분야 관심도*')
df = pd.DataFrame({
'분야': ['퍼포먼스 마케팅', '컨텍스트 마케팅', 'UGC 기반 브랜드 마케팅'],
'관심도': [20, 30, 50]
})
st.dataframe(df) 

st.write('*1-2 마케팅 분야별 정의*')

st.write('### 퍼포먼스 마케팅이란')
st.write('##### :red[성과]에 따라 광고에 대한 비용을 지불하는 마케팅으로 클릭 수, 전환율, ROAS(광고 수익률), CPA 등이 기준이 된다.')
st.write('')

st.subheader('전환율, ROAS 수식')

st.text('전환율')
st.latex(r'''
\text{Conversion Rate} = \frac{\text{전환 수}}{\text{방문자 수}} \times 100
''')

st.text('ROAS')
st.latex(r'''
\text{ROAS} = \frac{\text{광고 수익}}{\text{광고비}} \times 100
''')


st.write('### 컨텍스트 마케팅이란')
st.write('##### 사용자의 :blue[상황(맥락), 행동, 관심사]에 맞춰 개인화된 콘텐츠나 메시지를 제공하는 마케팅')
st.write('')

st.write('### UGC 기반 브랜드 마케팅이란')
st.write('##### :green[사용자가 만든 컨텐츠]를 기업의 신뢰도와 인지도 상승에 사용하는 마케팅')
st.write('')

import streamlit as st

st.write("1-3 📦 신제품 개발 및 시장 분석")


st.info("신제품 개발은 고객의 니즈 파악, 아이디어 발굴, 제품 설계 및 테스트, 상업화까지 이어지는 전략적 과정이다.", icon="ℹ️")


st.warning("시장 분석 없이 신제품을 출시하면 수요 부족, 경쟁 과열, 포지셔닝 실패 등의 리스크가 크다.", icon="⚠️")


st.error("타겟 시장 정의가 불명확하거나 경쟁자 분석이 미흡할 경우, 제품 실패 가능성이 높아진다.", icon="🚫")


st.success("철저한 시장 조사와 고객 인사이트 기반의 제품 개발은 성공적인 시장 진입과 매출 성장으로 이어질 수 있다.", icon="✅")

st.divider()

st.subheader('2. 관심있는 최신 경영 트렌드')

st.write('2-1 ESG 경영과 소비자 인식')

# ESG 경영 설명
st.info("""
- 기업들은 **탄소중립, 윤리적 노동, 투명한 지배구조**를 중심으로 ESG 경영을 강화하고 있습니다.
- ESG 활동은 단순한 이미지 개선을 넘어 **브랜드 충성도**, **소비 선택 요인**으로 이어지고 있습니다.
""", icon="ℹ️")

# 소비자 인식 변화
st.success("""
- 2025년 기준, 전체 소비자의 **68% 이상이 ESG를 고려해 제품/브랜드를 선택**하고 있습니다.
- 특히 **MZ세대**는 가격보다 **윤리성, 지속가능성**을 우선시하는 경향이 높습니다.
""", icon="✅")


st.write('2-2 📺 광고, sns 전략')


st.caption('제일제당 광고 영상')
st.audio("C:\\Users\\윤진이\\Desktop\\Documents\\python_st\\adv.mp3", format="audio/mpeg", loop=True)

st.info("""
CJ제일제당은 식품 브랜드를 중심으로 감성적이고 스토리텔링이 강한 광고를 선보여
소비자의 감정과 식문화 경험을 연결짓는 전략을 활용하고 있습니다.
""", icon="ℹ️")

st.caption('유명인을 통해 마케팅 유튜브 홍보')
video_file = open("C:\\Users\\윤진이\\Desktop\\Documents\\python_st\\marketing.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

st.success("""
CJ제일제당은 유명 연예인을 활용한 '축하 캠페인 영상'을 통해 브랜드 팬덤을 확대하고
YouTube 채널의 구독자 50만 돌파를 콘텐츠 마케팅의 성과로 연결했습니다.
""", icon="✅")

# 마케팅 전략 및 효과 설명
st.markdown("#### :orange[마케팅 전략 및 효과 설명]")

st.markdown("""
- **콘텐츠 중심 마케팅 (Content Marketing)**: 단순한 제품 홍보가 아닌 음식 문화와 일상 스토리를 중심으로 한 콘텐츠 제공.
- **인플루언서 마케팅**: 연예인(브랜드 모델)을 적극 활용해 유튜브/광고 영상의 도달 범위를 확대.
- **브랜드 팬덤화 전략**: 유튜브 채널을 통해 브랜드 팬층을 형성하고 구독자와 직접 소통.
- **성과**: 구독자 증가 → 브랜드 인지도 강화 → 매출 및 브랜드 충성도 상승.
""")


st.write("2-3 🍽️ 현대 식품 산업의 변화와 집중 영역")
st.markdown("#### :orange[현대 식품 산업은 '프리미엄 제품', '건강/기능성', '글로벌화'에 집중하고 있다.]")

st.info("""
- **가공식품** 분야는 HMR(가정간편식), 프리미엄 간편식에 집중 투자 중이다.
- **바이오 식품** 부문은 아미노산, 조미소재 등 B2B 기반 고기능성 원료 산업으로 확대 중이다.
- **F&C(Feed & Care)** 사업은 펫푸드 및 동물영양 분야에서 고성장세를 보이고 있다.
""", icon="ℹ️")

import streamlit as st
import pandas as pd
st.markdown("#### :orange[부문별 실적 변화 (2024년 vs 2025년 1분기)]")

data = {
    "분기": ["2024 Q【1】", "2025 Q1"],
    "식품사업": [11.353, 2.9246],        # 단위: 조 원
    "바이오사업": [4.2095, 0.8954],
    "Feed&Care (F&C)": [2.3085, 0.5425]
}

df = pd.DataFrame(data).set_index("분기")
df = df.astype(float)

st.line_chart(df)

st.divider()



from PIL import Image

st.subheader('3. 관심있는 기업, cj 제일제당')

st.write('제일제당 로고')
img = Image.open('C:\\Users\\윤진이\\Desktop\\Documents\\python_st\\logo.jpg')
st.image(img, width=300)

st.write('3-1 브랜드 파워와 혁신의 공존')

st.write("#### cj 제일제당은 '비비고', '햇반', '다시다'와 같이 오랜 시간 사랑받아온 브랜드를 어떻게 현대적으로 재해석하고 새로운 가치를 더하는 기업이다. 특히 **'비비고'의 글로벌 성공 사례**는 마케팅에 깊은 인사이트를 제공한다.")


st.write('3-2 📊 CJ제일제당 연도별 마케팅 비용 (단위: 백만 원)')

chart_data = pd.DataFrame({
    "연도": ["2015", "2016", "2017", "2018", "2019"],
    "마케팅비용(백만 원)": [1658512, 1942040, 2206432, 2020577, 2131096]
})


chart_data = chart_data.set_index("연도")

st.bar_chart(chart_data)

import streamlit as st
import pandas as pd

st.write("3-3 📊 CJ제일제당 다양한 사업 포트폴리오")

df = pd.DataFrame({
    '사업 분야': ['식품사업', '바이오사업', '건강 & 웰니스'],
    '핵심 제품/서비스': ['햇반, 비비고, 고메 등 가공식품', '아미노산, 조미소재, 단백질 원료', '건강기능식품, 맞춤형 영양 솔루션'],
    '주요 시장': ['국내 및 글로벌', '글로벌 (미국, 중국, 동남아 등)', '국내/글로벌 프리미엄 시장']
})

st.dataframe(df)


st.write("3-4 📈 CJ제일제당 포트폴리오 실적 변화(metric)")

col1, col2, col3 = st.columns(3)

col1.metric(label="식품사업 매출", value="4.2조원", delta="+6.5%")
col2.metric(label="바이오사업 매출", value="3.5조원", delta="-2.1%")
col3.metric(label="건강 & 웰니스", value="1.1조원", delta="+12.4%")

import streamlit as st
import pandas as pd

st.divider()

st.subheader('느낀점')

st.write('''
         CJ제일제당을 조사하며 단순한 식품회사가 아니라 콘텐츠와 ESG와 팬덤을 활용한 전략적 브랜드 기업이라는 점에 놀랐다.
마케팅이 단순한 홍보가 아닌 소통과 진정성의 싸움이라는 걸 느꼈고 나도 그런 브랜드를 만들고 싶다는 자극과 감동을 받았다.
최근 경영 트렌드와 맞물려, 기업이 사람처럼 말하고 행동해야 살아남는 시대라는 사실을 실감했다.
         ''')