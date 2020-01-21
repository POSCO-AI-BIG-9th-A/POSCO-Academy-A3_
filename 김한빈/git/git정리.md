# Git, Github 요약

#### A반 3조 김한빈

###### 1. Git이란?

협업 시 작업을 효율적으로 하기 위한 버전관리 툴. 이전에 만들어진 모든 변경사항의 "스냅샷"을 저장하여 이전 시점의 어떤 버전으로도 되돌릴 수 있게 만든다.

Git 사용 시 어려운 점은 명령어를 사용하여 접근해야 한다는 것이다.

Github는 2가지 방법으로 Git을 더 편리하게 사용할 수 있게 해준다. 

(1) Github 소프트웨어를 다운로드하면 로컬에서 사용자의 프로젝트를 관리할 수 있는 비주얼 인터페이스를 사용할 수 있다.

(2) Github.com에 계정을 생성하여 웹에서 프로젝트를 버전관리 할 수 있으며, 평가측정 등의 기능으로 일종의 SNS 같은 역할을 한다.

###### 2. 기본 용어

Command Line : 깃 명령어 입력 시 사용하는 컴퓨터 프로그램. 텍스트 기반 명령어를 입력한다.

Repository : 프로젝트가 live할 수 있는 디렉토리나 저장 공간. 주로 repo로 줄여서 사용. 사용자 컴퓨터 내 로컬 폴더가 될 수도 있고, Github나 다른 온라인 호스트의 저장 공간이 될 수도 있다.

Commit : 깃에게 파워를 주는 명령. 커밋하면 그 시점에 사용자 repo 스냅샷을 찍어 체크포인트로 활용할 수 있다.

Branch : 일반적으로 작업자들은 main project의 브랜치를 따와서(branch off), 자신이 변경하고 싶은 자신만의 버전을 만든다. 작업 후 메인디렉토리인 master에 브랜치를 merge한다.

###### 3. 주요 명령어

git init: 깃 저장소를 초기화 한다. 이 명령 실행 전까지는 repo나 디렉토리가 그냥 일반 폴더이다. 이것 입력 후 추가적인 깃 명령어들을 줄 수 있다.

git config: 처음 깃 설정시 유용

git help: 명령어 기능 확인 ex) git help init

git status: 저장소 상태 체크

gid add: 이 명령으로 새 파일이 repo에 추가되진 않는다. 대신 깃이 새 파일들을 '지켜보게' 한다. 파일을 추가하면 깃 repo 스냅샷에 포함된다.

git commit: 어떤 변경사항이라도 만든 후, 저장소의 '스냅샷'을 찍기 위해 입력. 가장 중요.  ex) git commit -m "Message hear."

git branch: 새로운 브랜치를 만들고, 자신만의 변경사항과 파일추가 등 커밋 타임라인을 만든다. ex) git branch cats

git checkout: 현재 위치하고 있지 않은 저장소를 "체크아웃"할 수 있다. ex) master브랜치를 들여다 보고 싶으면 'git checkout master' 사용

git merge: 브랜치에서 작업을 끝내고 모든 협업자가 볼 수 있는 master 브랜치로 병합 ex) git merge cats는 cats브랜치에서 만든 모든 변경사항을 master로 추가한다.

git push: 로컬 컴퓨터에서 작업하고 사용자의 커밋을 온라인으로도 볼 수 있기를 원한다면, 깃허브에 변경사항을 push한다.

git pull: 로컬 컴퓨터에서 작업시, 작업하고 있는 repo의 최신 버전을 원하면 깃허브로부터 변경사항을 pull한다.

###### 4. 처음으로 Git/Github 설정하기

(1) github.com 가입

(2) 터미널에서 git에 나의 이름과 이메일을 입력한다.(이메일은 github 메일과 동일)

(3) 온라인 repo 생성

(4) 로컬 저장소 생성

(5) 로컬 저장소와 깃허브 저장소 연결하기

###### 5. 로컬-온라인 연결 요약

git config --global user.name "이름"

git config --global user.email "깃허브 메일주소" // 매번 물어보는 귀찮음을 피하기 위해 설정.



mkdir ~/MyProject 		// 로컬 디렉토리 만들고

cd ~/MyProject			   // 디렉토리로 들어가서

git init							  // 깃 명령어를 사용할 수 있는 디렉토리로 만든다.

git status						 // 현재 상태를 훑어보고

git add 파일명.확장자	  //  깃 주목 리스트에 파일을 추가

git add .						   //  현재 디렉토리의 모든 파일을 추가

git commit -m "현재형으로 설명"  // 커밋해서 스냅샷을 찍는다.



git remote add origin https://github.com/username/myproject.git    // 로컬과 원격 저장소를 연결한다.

git remote -v  				 // 연결상태를 확인한다.

git push origin master	// 깃허브로 푸시한다.