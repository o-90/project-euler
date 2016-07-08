module Main where

------------------------------------------------------------------------------
-- In England the currency is made up of pound, £, and pence, p, and there
-- are eight coins in general circulation:
--
--     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
--
-- It is possible to make £2 in the following way:
--
--     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
--
-- How many different ways can £2 be made using any number of coins?
------------------------------------------------------------------------------

-- | recursive function to compute number of different ways to make chainge
-- | given an amount and coin denominations
numOfCoins :: Int -> [Int] -> Int
numOfCoins 0 _                   = 1
numOfCoins _ []                  = 0
numOfCoins money _  | money < 0  = 0
numOfCoins money coins@(x:xs)    = numOfCoins money xs + numOfCoins (money-x) coins

-- | main
main :: IO ()
main = do
  let ans = numOfCoins 200 [1, 2, 5, 10, 20, 50, 100, 200]
  print ans
