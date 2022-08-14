from bowling import Match
from bowling import Frame

def main():
    more = 'Y'
    first = ''
    second = ''
    while more == 'Y' or more == 'y':
        match = Match()
        
        for i in range(10):
            print("  Frame -", i + 1)
            frame = Frame()
            
            while frame.first < 0:
                first = int(input("\t Ball - 1: "))
                frame.setFirst(first)
                if frame.first < 0:
                    print("\t\t\t Invalid input, try again")
                if frame.isStrike():
                    print("\t\t\t\tCongratulations! It's a strike...")
                
            while frame.second < 0 and not frame.isStrike():
                second = int(input("\t Ball - 2: "))
                frame.setSecond(second)
                if frame.second < 0:
                    print("\t\t\t Invalid input, try again")
                if frame.isSpare():
                    print("\t\t\t\tCongratulations! It's a spare...")
                    
                match.addFrame(frame)

        # last frame
        frame = match.getFrame(10)
        if frame.isStrike() or frame.isSpare():
            # extra bowl
            if frame.isStrike() and 1  # extra bowl check
                # last bowl
        match.printScoreTable()

        
        
        more = input("\n\t\t Do more (Y/N) ? ")

main()
