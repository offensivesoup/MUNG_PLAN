from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker, providers
from random import choice
from community.models import Article, Comment

class DogProvider(providers.BaseProvider):
    def dog_concern(self):
        concerns = ['강아지가 밥을 잘 안 먹어요.', '강아지가 자꾸 짖어요.', '강아지 훈련에 어려움을 겪고 있어요.', '강아지와 잘 놀아줄 수 있는 방법이 뭐가 있을까요?', '강아지가 자꾸만 집안을 어지럽히네요.', '분리불안은 어떻게 하시나요?', '산책할 때마다 다른 강아지랑 싸우려고 해요..', '강아지가 물을 잘 안 먹어요',
                    '강아지 훈련은 어떻게 시키시나요?', '강아지가 사람을 무서워해요.', '강아지 멀미는 어떻게 하나요?', '목욕 잘 씻기는 법 있나요?', '강아지가 밤에 자꾸 깨요', '강아지 입질은 어떻게 하시나요?', '강아지가 벽을 자꾸 긁어요',
                    '강아지가 식탐이 너무 많아요', '강아지 비만은 어떻게 하나요', '미용을 할 때 스트레스 받는 강아지는 어떻게 하나요?', '특정 장소에 가는 걸 무서워해요..']
        return self.random_element(concerns)

    def dog_breed(self):
        breeds = ['말티즈', '푸들', '포메라니안', '시츄', '비숑프리제', '요크셔테리어', '진도견', '치와와', '스피츠', '닥스훈트', '리트리버']
        return self.random_element(breeds)

    def dog_name(self):
        names = ['뽀삐', '쫑이', '백구', '코코', '보리', '초코', '두부' ,' 호두', '별', '몽이', '까미', '망고', '똘이', '초롱이', '깜자', 
                 '뽀로로', '겨울이', '초롱이', '오복이', '김율', '가을이', '봄이', '여름이']
        return self.random_element(names)

    def dog_item(self):
        items = ['사료', '장난감', '영양제', '유모차', '그릇', '배변매트', '옷', '침대', '샴푸', '리드줄', '빗', '목욕용품', '간식', '쿠션', '이불', '장식품', '세척', '칫솔', '미용']
        return self.random_element(items)

    def korean_city(self):
        cities = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']
        return self.random_element(cities)

class Command(BaseCommand):
    help = 'create_data'
    
    def handle(self, *args, **options):
        faker = Faker('ko_KR')
        faker.add_provider(DogProvider)
        User = get_user_model()

        for _ in range(1000):  # 300개의 Article을 생성.
            user = User.objects.order_by('?').first()  # 랜덤한 User를 선택.
            category = faker.random_element(elements=('고민나누기', '중고장터', '동네사람들'))

            if category == '고민나누기':
                title1 = faker.dog_concern()
                content1 = f"우리 {faker.dog_name()} 걱정에 잠이 잘 안 오네요 ㅜㅜ"

                title2 = faker.dog_concern()
                content2 = f"조언 부탁드립니다 ㅜㅜ"
            elif category == '중고장터':
                title1 = f"{faker.dog_item()} 판매"
                content1 = f"{faker.dog_breed()} {faker.dog_name()}이(가) 사용하던 {faker.dog_item()} 나눔합니다."

                title2 = f"{faker.dog_item()} 나눔"
                content2 = f"{faker.dog_breed()} {faker.dog_name()}이(가) 사용하던 {faker.dog_item()} 판매합니다."
            else:
                title1 = f"{faker.korean_city()}에서 {faker.dog_breed()} 친구 찾아용"
                content1 = f"{faker.korean_city()}에 사는 {faker.dog_name()}이(가) 친구를 찾고 있어요."

                title2 = f"{faker.korean_city()}에서 {faker.dog_breed()} 친구 찾아용"
                content2 = f"{faker.korean_city()}에 산책 메이트 구해요."

            article = Article.objects.create(
                user=user,
                category=category,
                title=choice([title1, title2]),
                content=choice([content1, content2])
            )

            for _ in range(3):  # 각 Article에 대해 3개의 Comment를 생성합니다.
                comment_user = User.objects.order_by('?').first()  # 랜덤한 User를 선택합니다.
                comment_content1 = f"우리 {faker.dog_name()}도 그러네요 ㅜㅜ"
                comment_content2 = f"에고 걱정이 많으시겠어요 !!!!"
                comment_content3 = f"흠 그거 참 어려운 문제 같아요.."
                comment_content4 = f"이건 완전히 해결하기는 어려운 거 같아요..!"
                comment_content5 = f"유튜브에 행동 교정 영상 찾아보는 걸 추천해요!!"
                comment_content6 = f"스트레스를 해소시켜주시면 좋을 것 같아요!!"

                comment_content = choice([comment_content1, comment_content2, comment_content3, comment_content4, comment_content5, comment_content6])
                Comment.objects.create(
                    article=article,
                    user=comment_user,
                    content=comment_content,
                )

        self.stdout.write(self.style.SUCCESS('Data created successfully.'))