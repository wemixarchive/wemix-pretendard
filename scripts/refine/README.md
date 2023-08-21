# Refinement

완성 글꼴 파일을 생성하는 스크립트를 안내합니다.

## 필요 사양

#### 개발 환경
- zsh
- python3
- [fontTools](https://github.com/fonttools/fonttools)
- [afdko](https://github.com/adobe-type-tools/afdko)

## 완성 글꼴 파일 제작

다음과 같은 과정으로 Glyphs 3으로 제너레이트한 글꼴 파일을 완성 글꼴 파일로 만들 수 있습니다.

1. [WEMIXPretendard.glyphspackage](../../sources/README.md)로부터 글꼴 파일 제너레이트를 마쳤다면, 제너레이트한 글꼴 파일들을 이 디렉터리에 있는 [fonts](fonts) 디렉터리로 옮깁니다.
2. zsh로 `index.sh`를 실행합니다. 실행하기 전 필요 개발 환경이 모두 설치되었는지 확인하세요.
3. 정상적으로 스크립트가 동작한다면, 수정을 마친 글꼴 파일들은 [dist/public](../../packages/wemix-pretendard/dist/public)로 자동으로 옮겨집니다.

## 문의

스크립트에 대해 문의가 있다면 언제든지 orioncactus@gmail.com으로 알려주세요.
