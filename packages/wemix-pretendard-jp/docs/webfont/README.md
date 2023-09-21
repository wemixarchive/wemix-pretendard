# 웹폰트

대표적인 공개 CDN인 jsDelivr를 이용해 WEMIX Pretendard JP를 사용할 수 있습니다.

---

모든 기능을 포함한 WEMIX Pretendard JP를 웹폰트로 사용하려면 아래 코드를 사용하세요. 사용하는 font-family 이름은 `"WEMIX Pretendard JP"` 입니다.

#### HTML

```html
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/packages/wemix-pretendard-jp/dist/web/static/wemixpretendard-jp.css" />
```

#### CSS

```css
@import url("https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/packages/wemix-pretendard-jp/dist/web/static/wemixpretendard-jp.css");
```

---

### 다이나믹 서브셋

WEMIX Pretendard에서는 웹폰트 용량 문제를 해결하기 위한 방법으로 Google Fonts에서 제공하는 한글 글꼴과 동일한 방식으로 동적 서브셋을 제공합니다. 페이지에 포함된 글자만 선택적으로 다운로드해 보다 빠르게 WEMIX Pretendard JP를 사용하려면 아래 코드를 사용하세요. 사용하는 font-family 이름은 `"WEMIX Pretendard JP"` 입니다.

#### HTML

```html
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/packages/wemix-pretendard-jp/dist/web/static/wemixpretendard-jp-dynamic-subset.css" />
```

#### CSS

```css
@import url("https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/packages/wemix-pretendard-jp/dist/web/static/wemixpretendard-jp-dynamic-subset.css");
```

---

### 가변 다이나믹 서브셋

가변 다이나믹 서브셋으로 가변 Weight 속성과 함께 기존 다이나믹 서브셋보다 현저히 적은 용량으로 WEMIX Pretendard JP를 사용할 수 있습니다. 모던 브라우저에서 더욱 쾌적하게 WEMIX Pretendard JP를 사용하려면 아래 코드를 사용하세요. 사용하는 font-family 이름은 `"WEMIX Pretendard JP Variable"` 입니다.

#### HTML

```html
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/packages/wemix-pretendard-jp/dist/web/variable/wemixpretendardvariable-jp-dynamic-subset.css" />
```

#### CSS

```css
@import url("https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/packages/wemix-pretendard-jp/dist/web/variable/wemixpretendardvariable-jp-dynamic-subset.css");
```

---

### 가변 글꼴

가변 weight 속성을 사용하려면 아래 코드를 사용하세요. 사용하는 font-family 이름은 `"WEMIX Pretendard JP Variable"` 입니다.

#### HTML

```html
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/packages/wemix-pretendard-jp/dist/web/variable/wemixpretendardvariable-jp.css" />
```

#### CSS

```css
@import url("https://cdn.jsdelivr.net/gh/wemixarchive/wemix-pretendard@v1.0.0/packages/wemix-pretendard-jp/dist/web/variable/wemixpretendardvariable-jp.css");
```

---

### font-family

어디서든 동일한 환경을 가지고자 한다면 아래와 같은 font-family 구성을 추천합니다.

```css
font-family: "WEMIX Pretendard JP Variable", "WEMIX Pretendard JP", -apple-system, BlinkMacSystemFont, system-ui, Roboto, "Helvetica Neue", "Segoe UI", "Apple SD Gothic Neo", "Noto Sans KR", "Malgun Gothic", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", sans-serif;
```
