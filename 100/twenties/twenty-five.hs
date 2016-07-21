module Main where

-- 25)
-- The Fibonacci sequence is defined by the recurrence relation:
--
--     Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
--
-- Hence the first 12 terms will be:
--
--    F1 = 1
--    F2 = 1
--    F3 = 2
--    F4 = 3
--    F5 = 5
--    F6 = 8
--    F7 = 13
--    F8 = 21
--    F9 = 34
--    F10 = 55
--    F11 = 89
--    F12 = 144
--
-- The 12th term, F12, is the first term to contain three digits.  What is
-- the index of the first term in the Fibonacci sequence to contain 1000
-- digits?

-- ---------------------------------------------------------------------------
-- This is a great problem to utilize Memoization.  There is an excelent
-- tutorial at https://wiki.haskell.org/Memoization on using memoization with
-- and computing the Fibonacci Sequence.  This could be optimized further
-- by wrapping the recursion inside the fib function.  With each recursive call
-- to findNum, we are recomputing values that could be globally cached and
-- re-used.
-- ---------------------------------------------------------------------------

-- | Memoized Fibonacci
fib :: Int -> Integer
fib = (map fibonacci [0..] !!)
  where fibonacci 0 = 0
        fibonacci 1 = 1
        fibonacci n = fib (n-2) + fib (n-1)

-- | Function to convert an integer to a list of its numbers
-- | i.e.  123 -> [1, 2, 3]
digits :: Integer -> [Integer]
digits 0 = []
digits x = digits (x `div` 10) ++ [x `mod` 10]

-- | count the length of the digits in each list
numFibDigits :: Int -> Int
numFibDigits x = length $ digits $ fib x

-- | "iterate" until we find the first fibonacci number with 1000 digits
findNum :: (Int -> Int) -> Int -> Int -> Int
findNum f x n
  | function == n = x
  | otherwise     = findNum f (x+1) n
  where function  = f x

-- | main
main :: IO ()
main = do
  -- this is a rather naive seach.  We could start at something
  -- much bigger than two.
  let ans = findNum numFibDigits 2 1000
  print ans  -- 4782
