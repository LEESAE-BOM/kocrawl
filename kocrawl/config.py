CRAWLER = {
    'kinds': {
        'dust': ['미세먼지', '초미세먼지', '오존'],
        'rent':['대여할 곳']
    },
    'category':{
        'cycle': ["자전거", "따릉이", "새싹따릉이", "새싹 따릉이"],
        'car':["전기차", "전기자동차", "전기 자동차", "전기 차"],
    },

    'date': {
        'today': ['오늘', '지금', '현재'],
        'tomorrow': ['내일'],
        'after': ['모레', '내일모레'],
        'this_week': ['이번 주', '이번주', '금주', '금 주'],
        'specific': ['월', '월요일', '화', '화요일',
                     '수', '수요일', '목', '목요일',
                     '금', '금요일', '토', '토요일',
                     '일', '일요일']
    }
}

SEARCH = {
    'url': {
        'naver': 'https://search.naver.com/search.naver?ie=utf8&query=',
        'google': 'https://www.google.com/search?q=',
        'naver_map': 'https://map.naver.com/v5/api/search?caller=pcweb&query=',
        'daum_dict': 'https://100.daum.net/',
        'daum_news': 'https://news.daum.net/ranking/popular/',
        'rent_map':'https://pcmap.place.naver.com/place/list?query=',
        'naver_term':'https://terms.naver.com/'
    },
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'referer': 'http://google.com'
    }
}

EDIT = {
    'dust': {
        '좋음': '좋은 상태에요.',
        '보통': '보통 수준이에요.',
        '한때나쁨': '한 때 나쁠 수 있어요. 가급적 마스크를 챙기세요.',
        '나쁨': '나쁘네요. 외출시 마스크를 꼭 챙기세요.',
        '매우나쁨': '매우 심각해요. 집에 있는게 좋을 거에요.',
        '데이터없음': '아직 데이터가 없어요.'
    },

    'weather': {
        '흐림': '날씨가 약간 흐릴 수 있어요.',
        '맑음': '아마 하늘이 맑을 것 같아요.',
        '구름': '하늘에 구름이 껴있을 수도 있어요.',
        '구름조금': '구름이 살짝 낄 수도 있어요.',
        '구름많음': '구름이 많이 낀 날씨에요.',
        '구름많고 한때 비': '구름이 많이이 끼고 한때 비가 내릴 수 있어요.',
        '대체로맑음': '대체로 날씨가 맑을 것 같아요.',
        '대체로흐림': '날씨가 대체로 흐릴 것 같아요.',
        '흐리고비': '흐리고 가끔 비가 올 수도 있을 것 같아요.',
        '맑으나때때로구름': '하늘은 맑지만 때때로 구름이 있을 수 있어요.',
        '흐리고한때비': '하늘이 흐리고 때로 비가 올 수도 있어요.',
        '흐리고때때로갬': '하늘이 때때로 흐리지만 금방 갤 수도 있어요.',
        '안개': '안개가 껴서 앞이 잘 안보일 수도 있어요.',
        '소나기': '갑자기 소나기가 내릴 수도 있어요. 주의하세요.',
        '광역성소나기': '넓은 지역에 걸쳐서 광역성 소나기가 내릴 수도 있어요.',
        '국지성소나기': '좁은 지역에 한해서 국지성 소나기가 내릴 수도 있어요.',
        '광역성뇌우': '넓은 지역에 걸쳐서 광역성 뇌우가 있을 수도 있어요.',
        '국지성뇌우': '좁은 지역에 한해서 국지성 뇌우가 있을 수도 있어요.',
        '뇌우': '하늘에서 번개가 칠수도 있어요.',
        '천둥': '하늘에서 천둥이 칠 수도 있습니다.',
        '돌풍': '바람이 매우 심하게 불 수도 있어요.',
        '태풍': '태풍이 올 수도 있습니다. 위험할 수 있으니 조심하세요.',
        '허리케인': '허리케인이 올 수도 있습니다. 위험할 수 있으니 조심하세요.',
        '쓰나미': '쓰나미가 발생할 수도 있어요. 굉장히 위험하니 조심하세요.',
        '비': '비가 내릴 수 있습니다. 나가신다면 우산을 챙기세요.',
        '눈': '하늘에서 눈이 내릴 수 있어요. 따뜻하게 입으세요.',
        '폭설': '하늘에서 눈이 엄청 많이 내릴 수도 있어요. 따뜻하게 입으세요.',
        '비와눈': '비와 눈이 함께 내릴 수 있어요. 우산을 챙기세요.',
        '소낙눈': '갑자기 한번에 많은 눈이 내릴 수 있어요. 따뜻하게 입으세요.',
        '우박': '우박이 떨어질 수도 있어요. 조심하세요.',
        '흐리고 가끔 비': '날씨가 흐리고 가끔 비가 내릴 수도 있어요.',
        '데이터없음': '아직 데이터가 없어요.'
    }
}

ANSWER = {
    'dust_init': '{location}의 다양한 대기오염 정보를 전해드릴게요. 😀\n',
    'weather_init': '{location}의 날씨 정보를 전해드릴게요. 😉\n',
    'map_init': '{location}의 {place}에 대한 정보를 전해드릴게요!. 😀😀\n',
    'rent_init': '{location}의 {category} {item} 근처 정보를 전해드릴게요!. 😀😀\n',
    'fallback': "죄송해요.. 말씀하신 정보는 저도 잘 모르겠네요."
}
