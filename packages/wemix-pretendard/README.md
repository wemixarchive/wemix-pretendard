# WEMIX Pretendard

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/wemixarchive/wemix-pretendard/assets/7247848/95203349-b3e5-4d57-83dd-7b546b54fa6b">
  <img src="https://github.com/wemixarchive/wemix-pretendard/assets/7247848/2c4aee02-fd2b-4cb8-97c9-f308265be5b2" alt="Thumbnail">
</picture>

WEMIX Pretendard는 WEMIX 서비스에서 알맞게 쓸 수 있는 현대적인 글꼴입니다. [Pretendard](https://github.com/orioncactus/pretendard) 글꼴 가족 중 하나인 WEMIX Pretendard는 읽기 환경에서 향상된 가독성과 시각 보정을 위해 추가적인 작업을 하지 않아도 되며, UI 아이콘과 고정폭 기본 라틴을 추가적으로 지원합니다.

WEMIX Pretendard는 9가지 굵기로 제공되며, 가변 글꼴 또한 지원합니다.

## 다운로드

### [최신 버전 다운로드](https://github.com/wemixarchive/wemix-pretendard/releases/latest)

## 웹폰트

대표적인 공개 CDN인 jsDelivr를 이용해 WEMIX Pretendard를 사용할 수 있습니다.

---

모든 기능을 포함한 WEMIX Pretendard를 웹폰트로 사용하려면 아래 코드를 사용하세요. 사용하는 font-family 이름은 `"WEMIX Pretendard"` 입니다.

#### HTML

```html
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/dist/web/static/wemixpretendard.css" />
```

#### CSS

```css
@import url("https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/dist/web/static/wemixpretendard.css");
```

---

### 다이나믹 서브셋

Pretendard에서는 웹폰트 용량 문제를 해결하기 위한 방법으로 Google Fonts에서 제공하는 한글 글꼴과 동일한 방식으로 동적 서브셋을 제공합니다. 페이지에 포함된 글자만 선택적으로 다운로드해 보다 빠르게 WEMIX Pretendard를 사용하려면 아래 코드를 사용하세요. 사용하는 font-family 이름은 `"WEMIX Pretendard"` 입니다.

#### HTML

```html
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/dist/web/static/wemixpretendard-dynamic-subset.css" />
```

#### CSS

```css
@import url("https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/dist/web/static/wemixpretendard-dynamic-subset.css");
```

---

### 가변 다이나믹 서브셋

가변 다이나믹 서브셋으로 가변 Weight 속성과 함께 기존 다이나믹 서브셋보다 현저히 적은 용량으로 WEMIX Pretendard를 사용할 수 있습니다. 모던 브라우저에서 더욱 쾌적하게 WEMIX Pretendard를 사용하려면 아래 코드를 사용하세요. 사용하는 font-family 이름은 `"WEMIX Pretendard Variable"` 입니다.

#### HTML

```html
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/dist/web/variable/wemixpretendardvariable-dynamic-subset.css" />
```

#### CSS

```css
@import url("https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/dist/web/variable/wemixpretendardvariable-dynamic-subset.css");
```

---

### 가변 글꼴

가변 weight 속성을 사용하려면 아래 코드를 사용하세요. 사용하는 font-family 이름은 `"WEMIX Pretendard Variable"` 입니다.

#### HTML

```html
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/dist/web/variable/wemixpretendardvariable.css" />
```

#### CSS

```css
@import url("https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/dist/web/variable/wemixpretendardvariable.css");
```

---

### font-family

어디서든 동일한 환경을 가지고자 한다면 아래와 같은 font-family 구성을 추천합니다.

```css
font-family: "WEMIX Pretendard Variable", "WEMIX Pretendard", -apple-system, BlinkMacSystemFont, system-ui, Roboto, "Helvetica Neue", "Segoe UI", "Apple SD Gothic Neo", "Noto Sans KR", "Malgun Gothic", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", sans-serif;
```

## 크레딧

#### 바탕

[Pretendard](https://github.com/orioncactus/pretendard)

## 라이선스

WEMIX Pretendard는 [SIL 오픈 폰트 라이선스](https://scripts.sil.org/OFL)로 배포됩니다. 글꼴 단독 판매를 제외한 모든 상업적 행위 및 수정, 재배포가 가능합니다.
