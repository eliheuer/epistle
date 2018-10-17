import os 
import subprocess


try:
    print("**** Running Fontmake ******************************\n")
    subprocess.call(['fontmake', '-g', 'sources/E.glyphs', '-o', 'ttf',])
except:
    print("Error! Try installing Fontmake: https://github.com/googlei18n/fontmake")

print("\n**** Moving fonts to fonts directory *******************")
subprocess.call(['cp', 'master_ttf/Epistle-Regular.ttf', 'fonts/',])
print("     [+] Done")

print("\n**** Removing build directories  ***********************")
subprocess.call(['rm', '-rf', 'master_ttf', 'master_ufo',])
print("     [+] Done")

os.chdir("fonts")
cwd = os.getcwd()
print("     In Directory:", cwd)
print("\n**** Run: ttfautohint  *********************************\n")
subprocess.call(['ttfautohint', '-I', 'Epistle-Regular.ttf', 'Epistle-Regular-Fix.ttf'])
subprocess.call(['cp', 'Epistle-Regular-Fix.ttf', 'Epistle-Regular.ttf'])
subprocess.call(['rm', '-rf', 'Epistle-Regular-Fix.ttf'])
print("     [+] Done")

os.chdir("..")
cwd = os.getcwd()
print("     In Directory:", cwd)
print("\n**** Run: gftools  **************************************")
# subprocess.call(['gftools', 'fix-dsgi', 'fonts/Staatliches-Regular.ttf', '--autofix'])

