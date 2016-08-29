module Main where


-- | -------------------------------------------------------------------------
-- 77)
--
-- It is possible to write ten as the sum of primes in exactly five different
-- ways:
--
--     7 + 3
--     5 + 5
--     5 + 3 + 2
--     3 + 3 + 2 + 2
--     2 + 2 + 2 + 2 + 2
--
-- What is the first value which can be written as the sum of primes in over
-- five thousand different ways?
-- | -------------------------------------------------------------------------


import Data.Numbers.Primes


-- | same as coin changing problem (note: this is a naive implementation)
partitions :: Int -> [Int] -> Int
partitions 0 _           = 1
partitions _ []          = 0
partitions n _  | n < 0  = 0
partitions n ps@(x:xs)   = partitions n xs + partitions (n-x) ps

-- | product number of primes less than n
primesLessThan :: Int -> [Int]
primesLessThan n = takeWhile (< n) primes

-- | search for number where partitions is > 5000 for the first time
binarySearch :: Int -> Int -> Int -> Maybe Int
binarySearch want lo hi
  | hi < lo      = Just (mid+1)
  | f mid > want = binarySearch want lo (mid-1)
  | f mid < want = binarySearch want (mid+1) hi
  | otherwise    = Just mid
  where
    f x = partitions x (primesLessThan x)
    mid = lo + ((hi - lo) `div` 2)

-- | main
main :: IO ()
main = do
  let ans = binarySearch 5000 1 100
  print ans  -- 71
