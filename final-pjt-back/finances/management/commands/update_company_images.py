from django.core.management.base import BaseCommand
from finances.models import Deposit
import glob
import os

# Django의 커스텀 관리 명령어를 작성할 때는 BaseCommand 또는 AppCommand 클래스를 상속받는 Command 클래스를 정의
class Command(BaseCommand):
  def handle(self, *args, **options):
      # finances/static/finances 디렉토리에서 모든 PNG 파일을 검색.
      image_files = glob.glob('finances/static/finances/*.png')

      # 모든 Deposit 객체를 순회.
      for deposit in Deposit.objects.all():
          # 일치하는 이미지 파일을 찾아
          matching_files = [f for f in image_files if os.path.basename(f).replace('.png', '') in deposit.company_name]
          
          # 일치하는 파일이 있으면 해당 파일의 이름을 company_image 필드에 저장.
          if matching_files:
              deposit.company_image = os.path.basename(matching_files[0])
          # 일치하는 파일이 없으면 'bank.png'를 company_image 필드에 저장.
          else:
              deposit.company_image = 'bank.png'
          
          deposit.save()

      self.stdout.write(self.style.SUCCESS('Successfully updated company images'))