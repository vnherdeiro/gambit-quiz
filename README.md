# Gambit quiz

### [Gambit research](https://www.gambitresearch.com) offers an  [interview quiz](https://www.gambitresearch.com/quiz/) to reach them about their job opportunities. Here is my solution to the latest version of the puzzle (as of 04/2018).

The webpage shows the following:

> The cipher below contains instructions on how to apply for a job

> 90 78 175 126 88 111 50 44 178 128 80 181 115 93 184 126 74 183 123 88 177 133 9 169 129 91 99 133 88 175 136 82 177 121 9 183 122 78 99 89 74 176 116 82 183 50 76 171 115 85 175 119 87 170 119 23 99 98 85 168 115 92 168 50 92 168 128 77 99 139 88 184 132 9 182 129 85 184 134 82 178 128 9 164 128 77 99 85 63 99 134 88 99 123 76 164 128 76 178 118 78 131 121 74 176 116 82 183 132 78 182 119 74 181 117 81 113 117 88 176 50 90 184 129 93 172 128 80 99 132 78 169 119 91 168 128 76 168 76 9 123 66 30 115 115 74 116 73 34 118 64

and in the source code:

> 		<script type="text/javascript">
>		function scramble(ascii,a,b,c) {
>			for(i=0; i<ascii.length; i++) {
>				if (i%3==0) {ascii[i]=(ascii[i]+a)%256;}
>				if (i%3==1) {ascii[i]=(ascii[i]+b)%256;}
>				if (i%3==2) {ascii[i]=(ascii[i]+c)%256;}
>			}
>			return ascii;
>		}
>		</script>
		
which tells us that the cyphering was done by applying three different character value shifts, each shift being applied cyclically when iterating by character position.

Bottom line: to decipher we need to find `a`, `b` and `c` each in a `[0,255]` range.

Two similar solutions here:
-`solution.cpp`: brute force approach, attemps the 256*256*256 solutions and outputs the only which contains `gambit` in the deciphered message.
-`solution.py`: still a brute force approach, with a 256*3 complexity, again returns the only solution with output containing only acceptable characters.

Both return the same answer:

> a, b, c = 111, 167, 150

and the deciphered message:

> Hello, Congratulations for solving the Gambit challenge. Please send your solution and CV to icancode@gambitresearch.com quoting reference: f39968860d.