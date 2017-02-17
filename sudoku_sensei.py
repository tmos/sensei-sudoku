import Grid
import os
import time


def intro():

    step1 = """ \n \n
      sSSs   .S       S.    .S_sSSs      sSSs_sSSs     .S    S.    .S       S.
     d%%SP  .SS       SS.  .SS~YS%%b    d%%SP~YS%%b   .SS    SS.  .SS       SS.
    d%S'    S%S       S%S  S%S   `S%b  d%S'     `S%b  S%S    S&S  S%S       S%S
    S%|     S%S       S%S  S%S    S%S  S%S       S%S  S%S    d*S  S%S       S%S
    S&S     S&S       S&S  S%S    S&S  S&S       S&S  S&S   .S*S  S&S       S&S
    Y&Ss    S&S       S&S  S&S    S&S  S&S       S&S  S&S_sdSSS   S&S       S&S
    `S&&S   S&S       S&S  S&S    S&S  S&S       S&S  S&S~YSSY%b  S&S       S&S
      `S*S  S&S       S&S  S&S    S&S  S&S       S&S  S&S    `S%  S&S       S&S
       l*S  S*b       d*S  S*S    d*S  S*b       d*S  S*S     S%  S*b       d*S
      .S*P  S*S.     .S*S  S*S   .S*S  S*S.     .S*S  S*S     S&  S*S.     .S*S
    sSS*S    SSSbs_sdSSS   S*S_sdSSS    SSSbs_sdSSS   S*S     S&   SSSbs_sdSSS
    YSS'      YSSP~YSSY    SSS~YSSY      YSSP~YSSY    S*S     YSb   YSSP~YSSY
"""
    step2 = step1 + """ \n
          sSSs    sSSs   .S_sSSs      sSSs    sSSs   .S
         d%%SP   d%%SP  .SS~YS%%b    d%%SP   d%%SP  .SS
        d%S'    d%S'    S%S   `S%b  d%S'    d%S'    S%S
        S%|     S%S     S%S    S%S  S%|     S%S     S%S
        S&S     S&S     S%S    S&S  S&S     S&S     S&S
        Y&Ss    S&S_Ss  S&S    S&S  Y&Ss    S&S_Ss  S&S
        `S&&S   S&S~SP  S&S    S&S  `S&&S   S&S~SP  S&S
          `S*S  S&S     S&S    S&S    `S*S  S&S     S&S
           l*S  S*b     S*S    S*S     l*S  S*b     S*S
          .S*P  S*S.    S*S    S*S    .S*P  S*S.    S*S
        sSS*S    SSSbs  S*S    S*S  sSS*S    SSSbs  S*S
        YSS'      YSSP  S*S    SSS  YSS'      YSSP  S*S
    """

    os.system('clear')
    print(step1)
    time.sleep(.5)
    os.system('clear')
    print(step2)
    time.sleep(1)
    os.system('clear')

def main():
    """intro()"""
    # Create a new grid
    grid = Grid.Grid()
    # TODO set the original sudoku --> grid.set_sudoku()
    # Display the start sudoku
    grid.print_sudoku()
    # Ikuzo!
    grid.start_calculation()
    # Display the resolved sudoku
    grid.print_sudoku()

if __name__ == "__main__":
    main()
