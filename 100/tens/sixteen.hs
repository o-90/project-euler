module Main where

-- 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
-- What is the sum of the digits of the number 2^1000?

-- | get last digit from a number
lastDigit :: Integer -> Integer
lastDigit x = x `mod` 10

-- | chop off last digit from a number
dropLast :: Integer -> Integer
dropLast x = x `div` 10

-- | sum the digits of a number
sumDigits :: Integer -> Integer
sumDigits 0 = 0
sumDigits x = lastDigit x + sumDigits(dropLast x)

-- | main
main = do
  let ans = sumDigits (2^1000)
  print ans
