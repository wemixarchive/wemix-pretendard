const { FONTFAMILY, getFontList, subsets } = require("subset-utils");

const fontList = getFontList(FONTFAMILY.WEMIXPretendardJP);
const variable = getFontList(FONTFAMILY.WEMIXPretendardJP, { variable: true });

subsets(
    // WEMIX Pretendard JP woff
    ["static", "woff", fontList],
    ["dynamic", "woff", fontList],

    // WEMIX Pretendard JP woff2
    ["static", "woff2", fontList],
    ["dynamic", "woff2", fontList],

    // WEMIX Pretendard JP Variable
    ["static", "woff2", variable],
    ["dynamic", "woff2", variable]
);
