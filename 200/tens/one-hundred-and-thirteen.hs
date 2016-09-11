module Main where

-- |-------------------------------------------------------------------------
-- 113)
-- Working from left-to-right if no digit is exceeded by the digit to its left
-- it is called an increasing number; for example, 134468.Similarly if no digit
-- is exceeded by the digit to its right it is called a decreasing number;
-- for example, 66420.  We shall call a positive integer that is neither
-- increasing nor decreasing a "bouncy" number; for example, 155349.  As n
-- increases, the proportion of bouncy numbers below n increases such that
-- there are only 12951 numbers below one-million that are not bouncy and only
-- 277032 non-bouncy numbers below 1010.
-- How many numbers below a googol (10100) are not bouncy?
-- ---------------------------------------------------------------------------

-- |--------------------------------------------------------------------------
-- NOTE:  It can be shown that in an interval [10^(k-1), 10^k - 1] that there
-- are k+8 choose k decreasing numbers and k+9 choose k increasing numbers (
-- and there are 10 that are both).  
-- ---------------------------------------------------------------------------

binomial :: Integral a => a -> a -> a
binomial n k
  | k < 0 = 0
  | k > n  = 0
  | otherwise = fac n `div` (fac k * fac (n-k))
  where
  	fac j = product [1..j]

bouncy :: Integral a => a -> a
bouncy 0 = 0
bouncy k = binomial (k+8) k + binomial (k+9) k - 10

main :: IO ()
main = do
  let ans = sum [bouncy x | x <- [1..100]]
  print ans  -- 51161058134250
