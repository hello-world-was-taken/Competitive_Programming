# https://leetcode.com/problems/text-justification/


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        words_on_lines = self.prepare( words, maxWidth )
        spaces = self.calculateSpaceBetween( words_on_lines, maxWidth )
        ans = []
        
        for i, words_on_line in enumerate(words_on_lines[:-1]):
            curr = []
            space_spots = len( words_on_line ) - 1
            if space_spots > 0:
                if spaces[i] > space_spots:
                    space_size = spaces[i] // space_spots
                    isOdd = spaces[i] // space_spots == spaces[i] / space_spots
                else:
                    isOdd = True
                    space_size = 1

                for word in words_on_line:
                    curr.append( word )
                    curr.append( " " * min(spaces[i] + 1, space_size + 1))
                    spaces[i] = max( spaces[i] - space_size, 0 )
                    
                    if not isOdd:
                        isOdd = True
                        curr.append( " " )
                    
                curr.pop()  # remove the last space
                ans.append( "".join( curr ) )
            else:
                for word in words_on_line:
                    curr.append( word )
                    curr.append( " " )
                curr.pop()  # remove the last space
                ans.append( "".join( curr ) )
                sp = maxWidth - len( ans[-1] )
                ans[-1] += " " * sp
        
        ans.append( " ".join( words_on_lines[-1] ) )
        sp = maxWidth - len( ans[-1] )
        ans[-1] += " " * sp

        return ans
        
    def prepare(self, words, maxWidth) -> List[str]:
        curr_width = 0
        ans = []
        curr = []
        
        for word in words:
            
            # if the word and one additional space is able to fit
            if curr_width + len( word ) + 1 <= maxWidth:
                curr_width += len( word ) + 1
                curr.append( word )
            
            # if the word is able to fit making it the last word on the line
            elif curr_width + len( word ) <= maxWidth:
                curr_width += len( word )
                curr.append( word )
            
            else:
                ans.append( curr.copy() )
                curr_width = len( word ) + 1
                curr = [ word ]
        
        ans.append( curr )
        return ans
    
    
    def calculateSpaceBetween(self, words_on_lines, maxWidth):
        
        spaces = []
        
        for words_on_line in words_on_lines:
            length = 0
            # print(words_on_line)
            for word in words_on_line:
                length += len( word ) + 1
            
            length -= 1  # the last space is not needed
            total_spaces_on_line = maxWidth - length
            # print("spaces: ", total_spaces_on_line,"maxWidth: ", maxWidth,"length: ", length)
            spaces.append( total_spaces_on_line )
            
        return spaces
