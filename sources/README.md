# Sources

소스 파일 제작에 필요한 내용을 안내합니다.

## 필요 사양

#### 애플리케이션
- [Glyphs 3](http://glyphsapp.com)

## 구조

소스 파일은 다음과 같이 구성되어 있습니다:

1. `WEMIXPretendard.glyphspackage`: 완성 소스
2. `split`: 조각 소스 디렉터리
   1. `Pretendard.glyphspackage`: 바탕 소스
   2. `Pretendard-Split-Symbols-Base.glyphspackage`: WEMIX 아이콘 바탕 소스
   3. `Pretendard-Split-Symbols-WEMIX.glyphspackage`: 병합용 WEMIX Pretendard 소스
   4. `Pretendard-Split-Symbols.glyphspackage`: 병합용 WEMIX 아이콘 소스

## 완성 소스 제작

다음과 같은 과정으로 조각 소스 디렉터리로부터 완성 소스를 만들 수 있습니다.

1. 완성 소스인 `WEMIXPretendard.glyphspackage`를 제거합니다.
2. 바탕 소스인 `Pretendard.glyphspackage`를 완성 소스 위치에 복제하고, 이름을 `WEMIXPretendard.glyphspackage`로 바꿉니다.
3. 바꾼 소스를 Glyphs 3로 열고, 글꼴 정보를 수정합니다.
   - 글꼴 이름: `WEMIX Pretendard`로 대치
   - 디자이너: `Combined and redesigned to Pretendard by Kil Hyung-jin.` 부분을 `Combined and redesigned to Pretendard by Kil Hyung-jin; Customized to WEMIX Pretendard by Kil Hyung-jin.`로 대치
   - 저작권: `Copyright © 2023 Wemade Co., Ltd.` 및 `Copyright © 2023 위메이드`로 대치
   - 상표권: 가장 앞에 `WEMIX is a trademark of Wemade Co., Ltd.; ` 추가
5. 병합용 WEMIX Pretendard 소스에서 `glyphs` 디렉터리에 있는 모든 `.glyph` 파일을 복사합니다.
6. 복사한 `.glyph` 파일을 완성 소스인 `WEMIXPretendard.glyphspackage`에서 `glyphs` 디렉터리에 붙여넣습니다.
7. 병합용 WEMIX Pretendard 소스인 `Pretendard-Split-Symbols-WEMIX.glyphspackage`를 Glyphs 3으로 열고, 글꼴 정보 → Exports에서 각 Instance마다 정의된 Custom parameters를 복사합니다.
8. 완성 소스를 Glyphs 3로 열고, 복사한 Custom parameters를 5번과 같은 과정으로 각 Instance마다 붙여넣습니다.
9. 병합용 WEMIX 아이콘 소스도 병합용 WEMIX Pretendard 소스와 같은 과정을 진행해 글리프를 붙여넣고, Instance를 수정합니다. 단, 병합용 WEMIX Pretendard 소스와 중복된 Custom parameters가 있기 때문에, 중복된 Custom parameters는 기존 parameters에 이어 붙여넣습니다.

## 병합용 WEMIX 아이콘 소스 제작

다음과 같은 과정으로 WEMIX 아이콘 바탕 소스를 WEMIX Pretendard에 병합 가능한 소스로 만들 수 있습니다.

1. WEMIX 아이콘 바탕 소스인 `Pretendard-Split-Symbols-Base.glyphspackage`를 병합용 WEMIX 아이콘 소스인 `Pretendard-Split-Symbols.glyphspackage`로 복제합니다.
3. 복제한 병합용 WEMIX 아이콘 소스를 Glyphs 3로 열고, 글꼴 정보에서 Units per Em 오른쪽 Scale 아이콘 버튼을 눌러 Pretendard UPM인 2896으로 업데이트합니다.
4. 글꼴 정보 → Others에서 Grid Spacing을 `32`로, Subdivision을 `16`으로 바꿉니다.
5. 글꼴 목록에서 `symbolBase.large`와 `symbolBase.small`에서 폭을 각각 폭을 `3860`, `2412`으로 맞추고, 좌우 여백이 0인지 확인합니다.
6. Metrics out of sync가 표시되는 글리프는 모양을 조정해 sync가 되도록 맞춥니다.
7. 글꼴 정보 → Exports에 있는 `Master-Thin`과 `Master-Black` Instance를, 왼쪽 아래 `+` 버튼을 눌러 표시되는 `Instance as Master` 메뉴를 눌러 Master로 만듭니다.
8. Masters 탭으로 이동해 기존 `Thin`과 `Black` Master를 제거하고, 새로 만들어진 `Master-Thin`과 `Master-Black` Master를 기존 Master 이름으로 각각 바꿉니다.
9. Metrics out of sync로 표시되는 글리프를 `Update Metrics` 메뉴를 이용해 sync가 되도록 맞추고 저장합니다.
10. VS Code와 같은 코드 편집 애플리케이션으로 `Pretendard-Split-Symbols.glyphspackage`를 열고, Find and Replace 기능으로 완성 소스의 Master ID와 동일하도록 기존 Master ID를 일괄 변경해 맞춥니다.

## 글꼴 파일 제너레이트

다음과 같은 과정으로 완성 소스 파일에서 글꼴 파일을 생성할 수 있습니다.

1. File → Export... 메뉴를 누릅니다.
2. OTF 탭에서 File Format를 `.otf`만 설정하고, Options에서 `Remove Overlap`만 활성화해 글꼴을 내보냅니다. Outline Flavour는 무시하셔도 됩니다.
3. 글꼴을 내보냈다면, 글꼴 정보에서 Family Name 뒤에 ` Variable`을 붙이고, 다시 Export 메뉴를 실행합니다.
4. Variable Fonts 탭에서 File Format를 `.ttf`만 설정해 글꼴을 내보냅니다.
5. 이후 완성 글꼴 파일 생성과 관련한 내용은 [scripts](../scripts/README.md)로 이동해 확인하세요.

## WEMIX Pretendard JP 소스 제작

바탕 소스인 `PretendardJP.glyphspackage`를 바탕으로 WEMIX Pretendard와 동일한 과정으로 WEMIX Pretendard JP 소스를 만들 수 있습니다.

## 문의

소스 파일에 대해 문의가 있다면 언제든지 orioncactus@gmail.com으로 알려주세요.

