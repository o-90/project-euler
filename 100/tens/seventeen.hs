{-# OPTIONS_GHC -Wall #-}
module tester where

-- | change a number under 1000 to a word
numsToWords :: Int -> String
numsToWords x =
  if x > 1000 || x < 0
    then "?"
    else case x of
            _ | x == 1000 -> "onethousand"
            _ | x >  900  -> "ninehundredand"  ++ numsToWords (x - 900)
            _ | x == 900  -> "ninehundred"     ++ numsToWords (x - 900)
            _ | x >  800  -> "eighthundredand" ++ numsToWords (x - 800)
            _ | x == 800  -> "eighthundred"    ++ numsToWords (x - 800)
            _ | x >  700  -> "sevenhundredand" ++ numsToWords (x - 700)
            _ | x == 700  -> "sevenhundred"    ++ numsToWords (x - 700)
            _ | x >  600  -> "sixhundredand"   ++ numsToWords (x - 600)
            _ | x == 600  -> "sixhundred"      ++ numsToWords (x - 600)
            _ | x >  500  -> "fivehundredand"  ++ numsToWords (x - 500)
            _ | x == 500  -> "fivehundred"     ++ numsToWords (x - 500)
            _ | x >  400  -> "fourhundredand"  ++ numsToWords (x - 400)
            _ | x == 400  -> "fourhundred"     ++ numsToWords (x - 400)
            _ | x >  300  -> "threehundredand" ++ numsToWords (x - 300)
            _ | x == 300  -> "threehundred"    ++ numsToWords (x - 300)
            _ | x >  200  -> "twohundredand"   ++ numsToWords (x - 200)
            _ | x == 200  -> "twohundred"      ++ numsToWords (x - 200)
            _ | x >  100  -> "onehundredand"   ++ numsToWords (x - 100)
            _ | x == 100  -> "onehundred"      ++ numsToWords (x - 100)
            _ | x >= 90   -> "ninety"          ++ numsToWords (x - 90)
            _ | x >= 80   -> "eighty"          ++ numsToWords (x - 80)
            _ | x >= 70   -> "seventy"         ++ numsToWords (x - 70)
            _ | x >= 60   -> "sixty"           ++ numsToWords (x - 60)
            _ | x >= 50   -> "fifty"           ++ numsToWords (x - 50)
            _ | x >= 40   -> "forty"           ++ numsToWords (x - 40)
            _ | x >= 30   -> "thirty"          ++ numsToWords (x - 30)
            _ | x >= 20   -> "twenty"          ++ numsToWords (x - 20)
            _ | x == 19   -> "nineteen" 
            _ | x == 18   -> "eighteen" 
            _ | x == 17   -> "seventeen"
            _ | x == 16   -> "sixteen"  
            _ | x == 15   -> "fifteen"  
            _ | x == 14   -> "fourteen" 
            _ | x == 13   -> "thirteen" 
            _ | x == 12   -> "twelve"   
            _ | x == 11   -> "eleven"   
            _ | x == 10   -> "ten"      
            _ | x == 9    -> "nine"     
            _ | x == 8    -> "eight"    
            _ | x == 7    -> "seven"    
            _ | x == 6    -> "six"      
            _ | x == 5    -> "five"     
            _ | x == 4    -> "four"     
            _ | x == 3    -> "three"    
            _ | x == 2    -> "two"      
            _ | x == 1    -> "one"      
            _             -> ""

lenWords :: String -> Int
lenWords = length . numsToWords

print sum $ map lenWords [1..1000]
