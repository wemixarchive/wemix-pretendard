const { FONTFAMILY, getFontList, subsets } = require("subset-utils");

const fontList = getFontList(FONTFAMILY.WEMIXPretendard);
const variable = getFontList(FONTFAMILY.WEMIXPretendard, { variable: true });

subsets(
    // WEMIX Pretendard woff
    ["static", "woff", fontList],
    ["glyph", "woff", fontList],
    ["dynamic", "woff", fontList],

    // WEMIX Pretendard woff2
    ["static", "woff2", fontList],
    ["glyph", "woff2", fontList],
    ["dynamic", "woff2", fontList],

    // WEMIX Pretendard Variable
    ["static", "woff2", variable],
    ["dynamic", "woff2", variable]
);
