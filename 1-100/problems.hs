{-# OPTIONS_GHC -Wall #-}

-- Problem 48 ----------------------------------------------------------------
-- The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
--
-- Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
(sum $ map(\x -> x^x)[1,2 .. 1000]) `mod` 10^10
