#!/bin/zsh
set -e

################################
script_dir="$(cd "$(dirname "$0")" && pwd)"
font_path="$script_dir/fonts"
dist_path="$script_dir/../../../packages/wemix-pretendard/dist/public"
font_static_prefix="WEMIXPretendardJP-"
font_variable_prefix="WEMIXPretendardJPVariable"

################################
echo "Clear font name"
font_variable_useless_suffix="VF"
mv "$font_path/$font_variable_prefix$font_variable_useless_suffix.ttf" "$font_path/$font_variable_prefix.ttf"

################################
echo "Subroutinizing fonts..."
subroutinize_suffix_target=("otf")
subroutinize_suffix_cff=("CFF")
subroutinize_weight=("Thin" "ExtraLight" "Light" "Regular" "Medium" "SemiBold" "Bold" "ExtraBold" "Black")
for suffix in "${subroutinize_suffix_target[@]}"; do
    for name in "${subroutinize_weight[@]}"; do
        subroutinized=("Subroutinized");
        if [ -f "$font_path/$font_static_prefix$name.$suffix" ]; then
            cp "$font_path/$font_static_prefix$name.$suffix" "$font_path/$font_static_prefix$name$subroutinized.$suffix"
            tx -cff +S +b "$font_path/$font_static_prefix$name.$suffix" > "$font_path/$font_static_prefix$name.$subroutinize_suffix_cff"
            sfntedit -a CFF="$font_path/$font_static_prefix$name.$subroutinize_suffix_cff" "$font_path/$font_static_prefix$name$subroutinized.$suffix"
            rm "$font_path/$font_static_prefix$name.$suffix"
            rm "$font_path/$font_static_prefix$name.$subroutinize_suffix_cff"
            mv "$font_path/$font_static_prefix$name$subroutinized.$suffix" "$font_path/$font_static_prefix$name.$suffix"
        else
            echo "File missing: $subroutinize_target"
        fi
    done
done

################################
echo "Converting to ttx..."
for font_file in "$font_path"/*.(otf|ttf); do
    ttx "$font_file"
    rm "$font_file"
done

################################
echo "Fixing font values..."
python3 "$script_dir/fix.py"

################################
echo "Converting to otf/ttf..."
for font_file in "$font_path"/*.ttx; do
    ttx "$font_file"
    rm "$font_file"
done

################################
echo "Fixing Variable..."
for variable in "$font_path/$font_variable_prefix".ttf; do
    pyftsubset "$variable" \
        --glyphs='*' \
        --layout-features='*' --glyph-names --symbol-cmap --legacy-cmap \
        --notdef-glyph --notdef-outline --recommended-glyphs \
        --name-IDs='*' --name-legacy --name-languages='*'
    
    rm "$variable"
    mv "$font_path/$font_variable_prefix".subset.ttf "$variable"
done

################################
echo "Moving files to appropriate directories..."
for otf_file in "$font_path"/*.otf; do
    base_file=$(basename "$otf_file")
    mv -f "$otf_file" "$dist_path/static/$base_file"
done
for variable_file in "$font_path"/"$font_variable_prefix".*; do
    base_file=$(basename "$variable_file")
    mv -f "$variable_file" "$dist_path/variable/$base_file"
done
for ttf_file in "$font_path"/*.ttf; do
    if [ "$ttf_file" != "$font_path/$font_variable" ]; then
        base_file=$(basename "$ttf_file")
        mv -f "$ttf_file" "$dist_path/static/alternative/$base_file"
    fi
done

################################
echo "Done!"
