#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. She is biased towards her friends and may have distributed the chocolates unequally. One of the program managers gets to know this and orders Christy to make sure everyone gets equal number of chocolates.
But to make things difficult for the intern, she is ordered to equalize the number of chocolates for every colleague in the following manner,
For every operation, she can choose one of her colleagues and can do one of the three things.

1) She can give one chocolate to every colleague other than chosen one.
2 )She can give two chocolates to every colleague other than chosen one.
3 )She can give five chocolates to every colleague other than chosen one.
Result:
  Calculate minimum number of such operations needed to ensure that every colleague has the same number of chocolates.

Input Format
First line contains an integer denoting the number of testcases.  testcases follow.
Each testcase has lines. First line of each testcase contains an integer  denoting the number of colleagues. Second line contains N space separated integers denoting the current number of chocolates each colleague has.

Constraints
1 <= T <= 100
1 <= T <= 10000
Number of initial chocolates each colleague has < 1000

Output Format
 lines, each containing the minimum number of operations needed to make sure all colleagues have the same number of chocolates.

Sample Input

1 testcases
4 the number of colleagues
2 2 3 7  number of chocolates

Sample Output
2

Explanation
1st operation: Christy increases all elements by 1 except 3rd one
2 2 3 7 -> 3 3 3 8
2nd operation: Christy increases all element by 5 except last one
3 3 3 8 -> 8 8 8 8
'''
import sys
import timeit
def maxValue(items):
  maxIndex = len(items) - items[::-1].index(max(items)) - 1
  return items[maxIndex]

def getCase(selected, top):
  valid = lambda case, selected, top: (True if (selected+case) <= top else False)
  cases = [5, 2, 1]
  caseStudy = 0
  for case in cases:
    for item in selected:
      if(valid(case, item, top)):
        caseStudy = case
        break;
    if caseStudy:
      break;
  return caseStudy

def equal(chocolates):
  print('======')
  print(chocolates)
  top = chocolates[0]
  picked = maxValue(chocolates) or top
  startIndex = chocolates.index(picked)
  case = getCase(chocolates[startIndex:], picked)

  return [elem+case if not(startIndex == index) else elem for index, elem in enumerate(chocolates)]

if  __name__ =='__main__':
  start_time = timeit.default_timer()
  checkAllItems = lambda lst: lst[1:] == lst[:-1]
  testCaseNumber = 1
  testCaseList = []
  for test in range(int(testCaseNumber)):
    colleagues = 3187
    chocolates = '531 471 431 505 634 700 604 155 901 586 910 531 599 237 918 966 287 717 104 633 112 600 660 731 306 209 494 226 405 713 413 936 184 844 793 171 896 397 678 150 984 588 681 935 177 599 901 817 317 357 450 781 309 111 513 616 320 7 842 78 72 607 14 609 451 160 780 699 557 810 849 893 398 530 828 576 482 81 745 151 791 195 932 100 306 445 68 979 804 910 409 229 517 423 838 320 935 970 372 493 780 221 738 178 752 567 106 234 0 851 385 791 399 669 892 57 467 960 388 623 223 797 852 92 573 690 765 508 660 137 353 792 358 92 971 462 659 429 48 659 633 785 803 32 455 695 441 922 655 830 897 878 627 750 323 552 792 88 61 453 225 414 245 583 506 568 398 517 350 446 529 335 584 332 719 39 27 160 313 34 342 210 265 322 960 588 874 105 676 935 910 253 702 507 188 560 76 586 78 778 385 959 113 969 291 832 360 670 992 673 56 335 235 321 657 548 261 883 653 289 171 563 542 873 70 83 433 498 669 863 276 406 822 389 375 465 573 735 487 918 760 544 253 996 217 262 896 831 497 549 120 668 464 15 541 534 98 327 33 119 542 661 526 717 403 253 182 976 341 22 894 453 918 499 801 135 113 697 318 611 598 439 279 62 806 173 597 256 852 982 375 746 995 253 463 398 859 998 375 200 20 621 653 938 121 807 425 586 504 744 549 103 535 829 165 341 354 114 949 558 448 676 304 444 930 768 842 789 766 569 341 138 191 346 428 664 153 205 250 10 949 800 113 836 981 630 529 687 745 478 245 193 155 549 637 437 669 832 578 787 401 919 277 592 617 705 608 123 911 211 133 212 11 598 49 344 228 578 383 325 409 628 871 564 529 508 353 551 692 931 690 94 202 968 38 819 25 647 294 936 858 427 501 221 25 902 565 254 832 300 931 241 280 802 157 161 663 510 712 355 793 403 449 995 723 840 167 748 487 461 37 345 889 538 566 266 792 483 872 624 783 804 218 415 606 375 576 621 238 289 977 31 44 778 379 767 618 546 515 457 7 904 802 248 794 720 867 586 555 739 211 338 543 429 753 502 156 682 475 394 971 804 778 367 583 157 486 553 55 353 11 414 258 165 663 52 886 530 639 441 621 202 132 517 983 237 371 139 919 846 886 242 651 664 961 586 173 447 139 228 153 502 642 411 20 657 815 258 539 454 51 161 8 535 678 991 125 49 131 396 247 17 991 898 33 952 484 206 752 976 786 905 830 428 668 850 438 483 460 977 290 512 490 298 47 168 290 172 569 773 569 169 142 560 67 175 864 904 733 616 880 519 873 62 299 541 265 737 25 725 67 315 589 557 965 989 78 255 513 999 380 82 168 522 994 236 49 211 492 134 179 724 5 53 786 305 946 403 394 971 129 461 638 70 19 604 59 97 211 573 96 944 7 265 818 354 853 868 565 345 2 96 69 360 149 855 665 96 259 59 419 740 521 410 810 892 366 222 989 929 795 437 873 154 702 692 508 907 912 425 252 266 522 321 626 23 529 643 471 140 55 891 880 928 653 42 820 19 264 161 300 411 598 526 918 653 570 426 560 482 204 813 100 726 486 79 101 367 722 573 507 777 816 739 705 469 134 525 840 750 38 140 162 637 18 80 642 588 858 202 70 62 367 523 140 206 602 242 573 324 167 81 454 983 172 159 452 306 37 644 57 75 136 571 64 155 3 706 743 213 909 166 628 628 41 768 834 643 362 760 319 529 193 773 864 365 285 668 672 322 312 81 749 801 652 814 956 7 872 51 220 781 569 848 762 610 969 948 605 683 708 925 565 901 50 429 619 335 98 291 9 762 724 759 563 728 925 871 735 797 923 307 931 844 156 45 807 477 993 412 160 702 689 77 955 740 507 574 427 957 217 437 719 941 548 283 669 473 506 756 622 781 416 553 626 924 598 433 401 944 197 913 998 239 991 953 331 850 528 758 807 97 547 878 39 95 161 60 920 20 169 895 801 585 800 427 509 399 212 262 695 762 175 693 1 518 646 332 368 526 442 527 976 990 406 15 437 919 427 710 939 948 605 741 533 405 520 394 156 733 656 851 847 184 544 848 702 543 532 423 421 326 302 397 316 708 764 106 980 544 816 919 492 421 12 378 826 533 124 983 618 781 186 465 317 83 665 371 626 549 146 399 875 449 149 544 509 913 650 489 809 818 761 302 239 773 32 417 658 156 752 628 289 939 93 606 22 110 330 0 659 476 751 887 925 900 431 435 166 433 276 975 251 389 629 842 515 13 259 173 170 364 802 811 303 247 770 677 358 100 29 369 576 780 256 854 33 39 289 199 472 917 526 723 307 156 917 822 169 529 347 691 893 149 855 548 749 625 225 459 725 606 828 653 386 437 507 419 476 148 970 301 66 497 376 725 653 294 547 174 823 246 218 716 748 73 264 497 50 841 956 127 447 136 780 185 925 640 957 754 788 927 55 206 776 431 931 429 725 830 956 900 77 174 968 825 599 584 322 649 425 630 128 224 118 908 762 44 548 719 150 689 998 205 895 775 636 827 556 714 657 864 614 86 390 583 911 989 167 585 990 945 567 118 521 38 379 283 434 927 354 584 616 705 789 864 480 777 691 388 491 700 253 458 139 643 393 50 985 560 988 327 857 907 446 379 945 825 14 379 104 369 963 73 74 752 937 906 882 980 646 373 32 899 831 171 895 576 574 880 137 562 207 346 469 5 77 767 182 92 146 639 813 110 64 887 214 353 145 448 333 791 822 717 43 5 889 290 582 463 522 71 377 729 417 198 87 495 965 621 939 112 260 752 574 324 991 140 677 136 589 362 279 763 80 674 120 321 964 702 136 486 125 513 568 543 63 7 390 381 628 329 493 889 433 419 565 424 911 595 912 852 957 543 615 389 218 736 710 534 790 846 373 916 711 293 811 127 300 553 508 928 234 353 169 667 124 87 91 35 682 3 240 991 546 207 733 116 295 443 3 86 642 376 354 705 669 517 832 321 70 340 601 304 693 123 323 169 210 414 205 244 769 797 235 315 4 968 784 300 764 787 738 758 163 92 463 184 609 648 857 31 340 458 335 34 581 658 555 143 424 760 387 193 557 975 860 914 295 644 214 411 783 952 521 298 396 985 482 5 985 691 36 325 150 723 711 83 733 267 579 509 27 318 702 937 645 914 851 293 911 417 704 694 369 226 993 765 563 827 122 548 519 510 873 21 233 937 456 318 204 35 827 583 354 529 520 351 795 723 644 706 140 701 753 861 279 98 978 842 925 100 742 796 610 967 169 195 904 626 513 108 13 340 692 367 221 564 719 369 640 715 75 132 416 180 346 695 278 324 889 556 777 631 352 739 951 874 935 855 500 800 316 513 141 360 233 714 276 304 83 268 19 511 401 436 691 747 131 322 423 21 878 200 4 582 292 955 456 227 163 308 27 831 174 520 191 407 235 819 711 670 88 82 181 841 518 225 940 2 547 363 375 425 916 731 359 208 687 168 435 202 476 814 33 650 335 576 57 922 747 120 592 835 555 126 676 425 351 616 427 898 332 154 675 248 886 34 808 925 202 243 127 31 409 512 681 96 440 91 18 187 563 963 23 118 89 51 544 440 20 323 338 352 478 365 952 716 751 760 641 306 355 120 337 764 632 370 213 424 813 231 611 377 194 634 847 283 38 391 75 410 67 765 762 897 130 66 613 234 178 606 540 533 78 229 649 62 599 862 486 413 446 97 142 640 84 989 276 122 381 351 532 800 117 646 697 599 64 662 833 242 268 373 127 346 602 776 760 554 991 246 319 437 343 461 429 427 450 57 901 183 409 785 983 878 783 32 477 847 694 663 89 962 36 216 660 991 345 420 897 688 18 216 125 362 677 906 141 479 964 395 15 725 180 350 603 316 383 432 163 77 95 605 392 484 173 404 827 870 825 724 558 195 292 683 909 321 942 51 800 906 798 815 983 330 166 586 646 901 370 810 978 818 767 370 654 940 775 481 811 952 557 369 147 849 405 57 170 699 460 970 605 610 138 588 940 656 526 587 557 248 749 887 66 868 610 720 808 385 553 971 689 110 693 188 959 450 597 129 149 409 452 106 19 942 46 960 950 924 899 859 172 0 746 239 868 356 311 28 93 865 352 134 975 397 323 935 847 920 416 348 682 220 806 701 162 852 13 112 776 264 323 948 264 70 539 484 778 203 865 872 68 217 358 395 966 681 682 813 954 99 513 636 319 319 689 834 523 703 946 299 967 270 599 232 692 139 68 470 342 933 694 762 502 405 157 468 86 840 633 392 291 146 28 610 817 70 444 340 773 743 991 740 365 591 324 409 82 745 231 776 678 926 890 181 331 399 1 769 239 635 514 530 133 542 493 303 964 289 995 737 384 987 830 749 930 154 158 364 899 390 492 930 668 382 463 351 781 464 472 373 451 986 255 585 881 748 240 845 390 235 935 774 574 765 524 504 271 34 220 171 776 64 453 796 798 916 499 932 732 972 305 184 310 912 769 191 13 9 389 403 596 324 177 171 89 53 27 360 440 248 883 216 664 688 365 463 604 864 395 337 188 52 873 499 964 994 42 329 3 431 732 951 107 262 122 196 315 150 909 755 750 144 324 766 833 689 229 789 905 976 478 94 380 351 593 345 345 635 26 700 419 759 652 526 21 126 75 688 276 336 796 378 480 120 145 665 161 726 455 66 703 933 160 83 637 105 780 982 93 807 35 512 918 687 390 291 165 817 979 794 153 775 172 986 247 669 651 760 748 458 827 803 744 339 886 381 445 19 715 538 178 750 402 448 789 144 739 955 962 70 749 115 198 273 101 445 295 105 558 43 563 385 846 307 76 84 40 873 455 756 763 985 858 165 433 648 310 172 955 272 595 56 739 793 681 841 590 328 946 148 371 861 885 569 169 962 6 561 187 813 317 951 799 528 116 584 176 778 109 483 402 704 891 142 497 572 335 87 253 633 588 976 494 473 546 15 787 904 577 975 717 246 926 868 774 394 453 302 525 562 137 927 266 28 421 115 953 756 202 206 389 790 182 236 616 80 603 755 336 532 730 406 779 8 274 905 755 79 208 280 641 345 559 259 726 981 374 31 737 929 589 479 71 771 715 39 204 670 795 540 203 877 298 334 886 573 239 993 4 447 273 998 145 832 257 223 813 984 254 903 913 843 382 336 966 449 376 522 119 171 415 674 48 713 8 286 638 248 279 643 47 552 641 192 737 898 767 902 882 21 805 147 216 539 484 183 988 860 705 460 31 120 486 431 834 495 718 824 743 997 467 142 902 108 335 991 359 454 893 593 476 51 93 44 590 577 227 931 789 285 743 172 757 229 603 943 724 321 768 819 671 235 962 925 696 649 916 55 103 161 0 931 212 93 976 155 670 555 86 811 840 829 983 598 58 587 541 135 260 661 954 283 897 916 560 945 565 828 352 21 990 352 952 554 446 280 709 468 836 147 632 676 328 615 626 387 554 520 874 167 181 828 802 430 97 363 727 14 191 79 35 181 432 340 88 230 620 149 50 456 297 682 485 625 650 111 364 556 631 238 723 165 419 526 947 516 889 675 882 432 754 918 966 538 610 54 120 230 203 523 39 852 557 524 830 207 635 546 116 619 137 839 136 556 717 83 424 958 110 306 391 217 576 357 107 186 763 228 769 966 103 808 171 660 332 1 220 319 547 336 290 684 527 426 592 245 862 16 203 972 675 594 541 251 303 649 790 66 229 559 385 332 367 556 344 51 557 564 370 456 252 661 141 780 439 733 25 301 102 580 626 129 175 519 380 830 168 522 897 397 81 282 81 800 838 426 851 747 342 574 203 947 235 696 727 26 430 104 328 884 684 306 13 211 825 745 42 994 268 291 743 701 573 177 502 763 955 705 510 297 279 713 244 866 410 323 893 192 427 573 428 464 879 441 27 704 538 69 50 806 360 146 860 285 323 362 48 278 67 558 927 699 624 524 565 34 847 458 578 627 31 6 91 262 799 118 319 689 540 369 848 252 867 708 538 542 70 586 172 489 145 100 188 121 624 106 155 823 916 85 450 300 91 893 562 242 364 881 931 904 603 779 508 822 839 46 365 909 633 537 751 130 989 291 251 965 749 758 789 666 843 239 966 286 485 880 880 849 114 163 105 69 295 613 891 134 12 608 396 997 498 147 127 487 790 730 453 540 840 242 558 35 833 524 321 670 756 553 519 870 716 976 939 11 942 183 498 954 791 894 951 289 393 430 129 183 512 582 75 352 176 633 387 9 509 60 680 266 965 551 488 681 880 428 45 822 963 543 128 106 437 431 396 182 861 877 365 373 459 793 77 635 426 816 996 936 228 28 554 193 580 42 226 812 822 271 986 785 166 114 244 955 545 992 137 758 869 855 483 328 648 560 315 74 376 311 362 604 340 268 149 272 311 375 436 133 999 422 271 165 888 867 121 785 859 610 543 728 465 26 56 113 938 723 540 666 34 254 622 726 523 771 350 834 146 786 319 497 560 942 663 448 809 136 233 668 98 776 748 564 154 804 29 92 879 921 758 914 176 380 992 699 503 695 885 2 481 556 499 394 851 514 842 12 2 428 33 101 204 781 665 711 938 46 155 817 968 914 83 144 646 428 195 502 123 432 504 956 988 3 350 191 870 193 204 872 621 237 973 177 18 990 240 308 37 396 126 5 310 561 149 308 989 696 162 112 128 666 69 116 22 419 660 892 964 864 116 937 453 90 467 823 80 707 132 469 103 258 474 765 819 975 426 161 671 588 273 799 607 694 268 629 114 928 873 430 144 989 720 597 431 539 420 864 598 552 333 54 162 808 171 334 783 597 495 807 538 120 606 497 815 874 126 281 154 351 711 298 692 783 895 124 674 668 988 273 220 321 327 735 481 850 69 617 800 916 424 338 36 30 835 851 257 313 132 411 16 196 62 708 331 309 184 6 977 172 631 198 846 310 285 327 160 354 944 960 622 720 650 10 751 837 862 360 502 346 123 870 894 185 579 226 495 763 584 472 288 567 22 486 229 307 165 389 13 462 702 635 182 704 646 933 894 860 645 748 558 769 619 453 306 198 31 153 313 967 978 953 534 0 439 763 660 605 504 673 67 558 661 249 263 659 535 509 871 180 257 429 301 876 882 608 426 265 113 92 232 91 45 118 92 485 881 752 90 738 777 157 296 438 758 911 97 293 772'
    chocolates = [int(x) for x in chocolates.split()]
    testCaseList.append({
      "colleagues": colleagues,
      "chocolates": sorted(chocolates, reverse=True)
    })

  for testcase in testCaseList:
    result = testcase["chocolates"]
    colleague = testcase["colleagues"]
    operation = 0
    while not (checkAllItems(result)):
      result = equal(result)
      operation += 1
    elapsed = timeit.default_timer() - start_time
    sys.stdout.write('{0}'.format(operation))
    print(elapsed)
    sys.stdout.write('\n')