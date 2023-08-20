import os

script_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(script_dir, 'fonts/')


def process_file(file_path, replacements):
    with open(file_path, 'r') as file:
        filedata = file.read()

    for search, replace in replacements.items():
        filedata = filedata.replace(search, replace)

    with open(file_path, 'w') as file:
        file.write(filedata)


file_suffixes = [
    '-Thin', '-ExtraLight', '-Light', '-Regular', '-Medium',
    '-SemiBold', '-Bold', '-ExtraBold', '-Black', 'Variable',
    '-Thin#1', '-ExtraLight#1', '-Light#1', '-Regular#1',
    '-Medium#1', '-SemiBold#1', '-Bold#1', '-ExtraBold#1', '-Black#1'
]

file_replacements_list = [
    {
        '<underlinePosition value="-337"/>': '<underlinePosition value="-307"/>',
        '<UnderlinePosition value="-367"/>': '<UnderlinePosition value="-337"/>'
    },
    {
        '<underlinePosition value="-334"/>': '<underlinePosition value="-291"/>',
        '<UnderlinePosition value="-377"/>': '<UnderlinePosition value="-334"/>'
    },
    {
        '<underlinePosition value="-330"/>': '<underlinePosition value="-274"/>',
        '<UnderlinePosition value="-386"/>': '<UnderlinePosition value="-330"/>'
    },
    {
        '<underlinePosition value="-327"/>': '<underlinePosition value="-258"/>',
        '<UnderlinePosition value="-396"/>': '<UnderlinePosition value="-327"/>'
    },
    {
        '<underlinePosition value="-321"/>': '<underlinePosition value="-244"/>',
        '<UnderlinePosition value="-398"/>': '<UnderlinePosition value="-321"/>'
    },
    {
        '<underlinePosition value="-314"/>': '<underlinePosition value="-228"/>',
        '<UnderlinePosition value="-400"/>': '<UnderlinePosition value="-314"/>'
    },
    {
        '<underlinePosition value="-308"/>': '<underlinePosition value="-214"/>',
        '<UnderlinePosition value="-402"/>': '<UnderlinePosition value="-308"/>'
    },
    {
        '<underlinePosition value="-302"/>': '<underlinePosition value="-200"/>',
        '<UnderlinePosition value="-404"/>': '<UnderlinePosition value="-302"/>'
    },
    {
        '<underlinePosition value="-296"/>': '<underlinePosition value="-186"/>',
        '<UnderlinePosition value="-406"/>': '<UnderlinePosition value="-296"/>'
    },
    {
        '<underlinePosition value="-327"/>': '<underlinePosition value="-258"/>',
        'CTUS;WEMIXPretendardVariable-Regular': 'CTUS;WEMIXPretendardVariable',
        '<!-- Thin -->\n    <!-- PostScript: PretendardVariable-Thin -->\n    <NamedInstance flags="0x0" postscriptNameID="258" subfamilyNameID="257">\n      <coord axis="wght" value="100.0"/>\n    </NamedInstance>\n\n    <!-- ExtraLight -->\n    <!-- PostScript: PretendardVariable-ExtraLight -->\n    <NamedInstance flags="0x0" postscriptNameID="260" subfamilyNameID="259">\n      <coord axis="wght" value="200.0"/>\n    </NamedInstance>\n\n    <!-- Light -->\n    <!-- PostScript: PretendardVariable-Light -->\n    <NamedInstance flags="0x0" postscriptNameID="262" subfamilyNameID="261">\n      <coord axis="wght" value="300.0"/>\n    </NamedInstance>\n\n    <!-- Regular -->\n    <!-- PostScript: PretendardVariable-Regular -->\n    <NamedInstance flags="0x0" postscriptNameID="6" subfamilyNameID="2">\n      <coord axis="wght" value="400.0"/>\n    </NamedInstance>\n\n    <!-- Medium -->\n    <!-- PostScript: PretendardVariable-Medium -->\n    <NamedInstance flags="0x0" postscriptNameID="264" subfamilyNameID="263">\n      <coord axis="wght" value="500.0"/>\n    </NamedInstance>\n\n    <!-- SemiBold -->\n    <!-- PostScript: PretendardVariable-SemiBold -->\n    <NamedInstance flags="0x0" postscriptNameID="266" subfamilyNameID="265">\n      <coord axis="wght" value="600.0"/>\n    </NamedInstance>\n\n    <!-- Bold -->\n    <!-- PostScript: PretendardVariable-Bold -->\n    <NamedInstance flags="0x0" postscriptNameID="268" subfamilyNameID="267">\n      <coord axis="wght" value="700.0"/>\n    </NamedInstance>\n\n    <!-- ExtraBold -->\n    <!-- PostScript: PretendardVariable-ExtraBold -->\n    <NamedInstance flags="0x0" postscriptNameID="270" subfamilyNameID="269">\n      <coord axis="wght" value="800.0"/>\n    </NamedInstance>\n\n    <!-- Black -->\n    <!-- PostScript: PretendardVariable-Black -->\n    <NamedInstance flags="0x0" postscriptNameID="272" subfamilyNameID="271">\n      <coord axis="wght" value="900.0"/>\n    </NamedInstance>\n\n    <!-- Thin -->\n    <!-- PostScript: PretendardVariable-Thin -->\n    <NamedInstance flags="0x0" postscriptNameID="258" subfamilyNameID="257">\n      <coord axis="wght" value="100.0"/>\n    </NamedInstance>\n\n    <!-- ExtraLight -->\n    <!-- PostScript: PretendardVariable-ExtraLight -->\n    <NamedInstance flags="0x0" postscriptNameID="260" subfamilyNameID="259">\n      <coord axis="wght" value="200.0"/>\n    </NamedInstance>\n\n    <!-- Light -->\n    <!-- PostScript: PretendardVariable-Light -->\n    <NamedInstance flags="0x0" postscriptNameID="262" subfamilyNameID="261">\n      <coord axis="wght" value="300.0"/>\n    </NamedInstance>\n\n    <!-- Regular -->\n    <!-- PostScript: PretendardVariable-Regular -->\n    <NamedInstance flags="0x0" postscriptNameID="6" subfamilyNameID="2">\n      <coord axis="wght" value="400.0"/>\n    </NamedInstance>\n\n    <!-- Medium -->\n    <!-- PostScript: PretendardVariable-Medium -->\n    <NamedInstance flags="0x0" postscriptNameID="264" subfamilyNameID="263">\n      <coord axis="wght" value="500.0"/>\n    </NamedInstance>\n\n    <!-- SemiBold -->\n    <!-- PostScript: PretendardVariable-SemiBold -->\n    <NamedInstance flags="0x0" postscriptNameID="266" subfamilyNameID="265">\n      <coord axis="wght" value="600.0"/>\n    </NamedInstance>\n\n    <!-- Bold -->\n    <!-- PostScript: PretendardVariable-Bold -->\n    <NamedInstance flags="0x0" postscriptNameID="268" subfamilyNameID="267">\n      <coord axis="wght" value="700.0"/>\n    </NamedInstance>\n\n    <!-- ExtraBold -->\n    <!-- PostScript: PretendardVariable-ExtraBold -->\n    <NamedInstance flags="0x0" postscriptNameID="270" subfamilyNameID="269">\n      <coord axis="wght" value="800.0"/>\n    </NamedInstance>\n\n    <!-- Black -->\n    <!-- PostScript: PretendardVariable-Black -->\n    <NamedInstance flags="0x0" postscriptNameID="272" subfamilyNameID="271">\n      <coord axis="wght" value="900.0"/>\n    </NamedInstance>': '<!-- Thin -->\n    <!-- PostScript: PretendardVariable-Thin -->\n    <NamedInstance flags="0x0" postscriptNameID="258" subfamilyNameID="257">\n      <coord axis="wght" value="100.0"/>\n    </NamedInstance>\n\n    <!-- ExtraLight -->\n    <!-- PostScript: PretendardVariable-ExtraLight -->\n    <NamedInstance flags="0x0" postscriptNameID="260" subfamilyNameID="259">\n      <coord axis="wght" value="200.0"/>\n    </NamedInstance>\n\n    <!-- Light -->\n    <!-- PostScript: PretendardVariable-Light -->\n    <NamedInstance flags="0x0" postscriptNameID="262" subfamilyNameID="261">\n      <coord axis="wght" value="300.0"/>\n    </NamedInstance>\n\n    <!-- Regular -->\n    <!-- PostScript: PretendardVariable-Regular -->\n    <NamedInstance flags="0x0" postscriptNameID="6" subfamilyNameID="2">\n      <coord axis="wght" value="400.0"/>\n    </NamedInstance>\n\n    <!-- Medium -->\n    <!-- PostScript: PretendardVariable-Medium -->\n    <NamedInstance flags="0x0" postscriptNameID="264" subfamilyNameID="263">\n      <coord axis="wght" value="500.0"/>\n    </NamedInstance>\n\n    <!-- SemiBold -->\n    <!-- PostScript: PretendardVariable-SemiBold -->\n    <NamedInstance flags="0x0" postscriptNameID="266" subfamilyNameID="265">\n      <coord axis="wght" value="600.0"/>\n    </NamedInstance>\n\n    <!-- Bold -->\n    <!-- PostScript: PretendardVariable-Bold -->\n    <NamedInstance flags="0x0" postscriptNameID="268" subfamilyNameID="267">\n      <coord axis="wght" value="700.0"/>\n    </NamedInstance>\n\n    <!-- ExtraBold -->\n    <!-- PostScript: PretendardVariable-ExtraBold -->\n    <NamedInstance flags="0x0" postscriptNameID="270" subfamilyNameID="269">\n      <coord axis="wght" value="800.0"/>\n    </NamedInstance>\n\n    <!-- Black -->\n    <!-- PostScript: PretendardVariable-Black -->\n    <NamedInstance flags="0x0" postscriptNameID="272" subfamilyNameID="271">\n      <coord axis="wght" value="900.0"/>\n    </NamedInstance>'
    },
    {
        '<underlinePosition value="-337"/>': '<underlinePosition value="-307"/>',
        '<UnderlinePosition value="-367"/>': '<UnderlinePosition value="-337"/>'
    },
    {
        '<underlinePosition value="-334"/>': '<underlinePosition value="-291"/>',
        '<UnderlinePosition value="-377"/>': '<UnderlinePosition value="-334"/>'
    },
    {
        '<underlinePosition value="-330"/>': '<underlinePosition value="-274"/>',
        '<UnderlinePosition value="-386"/>': '<UnderlinePosition value="-330"/>'
    },
    {
        '<underlinePosition value="-327"/>': '<underlinePosition value="-258"/>',
        '<UnderlinePosition value="-396"/>': '<UnderlinePosition value="-327"/>'
    },
    {
        '<underlinePosition value="-321"/>': '<underlinePosition value="-244"/>',
        '<UnderlinePosition value="-398"/>': '<UnderlinePosition value="-321"/>'
    },
    {
        '<underlinePosition value="-314"/>': '<underlinePosition value="-228"/>',
        '<UnderlinePosition value="-400"/>': '<UnderlinePosition value="-314"/>'
    },
    {
        '<underlinePosition value="-308"/>': '<underlinePosition value="-214"/>',
        '<UnderlinePosition value="-402"/>': '<UnderlinePosition value="-308"/>'
    },
    {
        '<underlinePosition value="-302"/>': '<underlinePosition value="-200"/>',
        '<UnderlinePosition value="-404"/>': '<UnderlinePosition value="-302"/>'
    },
    {
        '<underlinePosition value="-296"/>': '<underlinePosition value="-186"/>',
        '<UnderlinePosition value="-406"/>': '<UnderlinePosition value="-296"/>'
    }
]

for suffix, file_replacements in zip(file_suffixes, file_replacements_list):
    file_path = os.path.join(folder_path, f'WEMIXPretendard{suffix}.ttx')
    process_file(file_path, file_replacements)
