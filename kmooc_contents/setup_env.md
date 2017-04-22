## OR Python 환경 설정
### Pre-Requisite
OR Python 코딩 환경 설정을 위해서는 사전에 아래와 같은 지식이 필요함
- Miniconda 설치 관련
    - 윈도우즈: https://youtu.be/OMuHLDvmQl4?list=PLBHVuYlKEkUJvRVv9_je9j3BpHwGHSZHz
    - 우분투: https://youtu.be/kKoYbDWvHdo?list=PLBHVuYlKEkUJvRVv9_je9j3BpHwGHSZHz
    - Mac OS: https://youtu.be/WsQ-4QDQxAQ?list=PLBHVuYlKEkUJvRVv9_je9j3BpHwGHSZHz
- Conda 가상 환경 설정 관련
    - Overview - [강의영상](https://www.youtube.com/watch?v=iV_1dal69Xc&list=PLBHVuYlKEkUJvRVv9_je9j3BpHwGHSZHz&index=50), [강의자료](https://doc.co/uJ7H6L/EFk5T6)
    - Modules - [강의영상](https://www.youtube.com/watch?v=vJ3kEhB_ERE&list=PLBHVuYlKEkUJvRVv9_je9j3BpHwGHSZHz&index=51), [강의자료](https://doc.co/qNxUN1/EFk5T6)
    - Packages - [강의영상](https://www.youtube.com/watch?v=nWAomgvxihg&index=42&list=PLBHVuYlKEkUJvRVv9_je9j3BpHwGHSZHz), [강의자료](https://doc.co/hXxeLm/EFk5T6)
    - 가상환경과 Package 활용하기 - [강의영상](https://www.youtube.com/watch?v=QLF5UvUvKCo&list=PLBHVuYlKEkUJvRVv9_je9j3BpHwGHSZHz&index=51), [강의자료](https://doc.co/SoCj3W/EFk5T6)

### Channel 수정
최근 업데이트된 Conda 환경은 `윈도우`에 한해 오류가 발생하고 있음. 수행전 반드시 다음 명령어를 `CMD 창`에서 실행시킨 후 모듈을 설치할 것
```commandline
conda config --add channels conda-canary
conda update conda
```

### 가상환경 설정 및 모듈 설치
다음으로 모듈 설치를 위한 기본 가상환경을 설정, 본 강의 영상에 이미 수록된 내용임

- conda 가상환경 만들기
```commandline
conda create -n or_kmooc python=3.5
```

- 설치완료 후 conda 가상환경 실행 및 해제
```commandline
activate or_kmooc # 가상환경 실행
deactivate or_kmooc # 가상환경 해제시 필요한 명령어
```

- 필요한 모듈 설치하기
```commandline
activate kibo_project # 가상환경 실행상태에서 시작
conda install numpy
conda install jupyter
conda install matplotlib
```