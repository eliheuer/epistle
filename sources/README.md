# Source Notes

The `ttf` file is built from source using the following command from the root directory:

```
py sources/BUILD.py && gftools fix-dsig fonts/Epistle-Regular.ttf --autofix
```

Dependencies installed should include:

 - [fontmake](https://github.com/googlei18n/fontmake)
 - [gftools](https://github.com/googlefonts/gftools)
 - [ttfautohint](https://www.freetype.org/ttfautohint/)

