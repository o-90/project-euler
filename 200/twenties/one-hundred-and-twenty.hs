module Main (main) where

-- | -------------------------------------------------------------------------
-- 120)
-- Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.  For
-- example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 ≡ 42 mod 49. And
-- as n varies, so too will r, but for a = 7 it turns out that rmax = 42.
-- For 3 ≤ a ≤ 1000, find ∑ rmax.
-- ---------------------------------------------------------------------------
-- NOTE: Using the binomial theorem, we can expand (a-1)^n and (a+1)^n as - if
-- n is even -> 2*[nC0 + nC2*a^2+nC4*a^4 + ....].  So, r = 2 for all n even.
-- If n is odd -> 2*[nC1*a + nC3*a^3 + nC5*a^5 + ...].  So r will be
-- 2*n*a if 2*n*a < a^2 else 2*n*a % a^2.
-- ---------------------------------------------------------------------------


squares :: Int -> Int
squares 2 = 0
squares n = func n + squares (n-1)
  where
    func :: Int -> Int
    func k = maximum $ map (\x -> 2*x*k `mod` m) (take k [1,3..])
      where
        m = k*k


main :: IO ()
main = do
    let ans = squares 1000
    print ans  -- 333082500
