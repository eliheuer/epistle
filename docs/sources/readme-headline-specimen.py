# Render this specimen with DrawBot3: http://www.drawbot.com/

# Import modules:
import math

#Import pages
import pages.page001

# Basic variables  (width, height, ):
W, H, M, F = 1920, 1080, 128, 32

# Load font and print font info:
# print(installedFonts(supportsCharacters=None))
font("fonts/amiri/Amiri-Bold.ttf")


# Draw a grid from a given increment:
def grid(inc):

    stpX, stpY = 0, 0  # Step in sequence on x axis
    incX, incY = inc, inc  # Grid increment
    
    stroke(0.6, 0, 0)  # Set grid line color RED
    for x in range(int(((W-(M*2))/inc+1 ))):
        polygon((M+stpX, M), (M+stpX, H-(M-8)))
        stpX += incX  # Set position for next gridline

    stroke(0, 0, 0.6)  # Set grid line color BLUE      
    for y in range(int(((H-(M*2))/inc)+2)):
        polygon((M, M+stpY), (W-M, M+stpY))
        stpY += incY  # Set position for next gridline


# Title Page #####################################################
newPage(W, H)
fill(1)           # Set the background color
rect(0, 0, W, H)  # Draw the background
# grid(32)        # Draw the grid
font("fonts/Epistle-Regular.ttf")  # Set the font

# Basic Style
stroke(None)
fill(0)
fontSize(150)
lh = 32*5

# Headline
text("Epistle", (M, (H-(88))-(1*lh)), align="left")
text("ABCDEFGHIJKLMNO", (M, (H-(88))-(2*lh)), align="left")
text("PQRSTUVWXYZ.,;:@", (M, (H-(88))-(3*lh)), align="left")
text("abcdefghijklmnopqrstu", (M, (H-(88))-(4*lh)), align="left")
text("vwxyz1234567890!?&*", (M, (H-(88))-(5*lh)), align="left")

# Save PDF
saveImage("readme-headline-specimen.png")