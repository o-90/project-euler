module Main where

-- |--------------------------------------------------------------------------
-- 85)
-- By counting carefully it can be seen that a rectangular grid measuring 3
-- by 2 contains eighteen rectangles:
--
--     6, 4, 2, 3, 2, 1
--
-- Although there exists no rectangular grid that contains exactly two
-- million rectangles, find the area of the grid with the nearest
-- solution.
-- |--------------------------------------------------------------------------


import Data.PQueue.Prio.Min (fromList, findMin)


triangle :: Fractional a => a -> a -> a
triangle x y = (x)*(y)*(x+1)*(y+1) / 4

findSquares :: (Fractional a, Ord a) => a -> [(a, (a, a))]
findSquares 1  = []
findSquares sq = aux 1 sq ++ aux 1 (sq-1)
  where
    aux x n
      | n <= x    = []
      | otherwise = [(createKey x n, (x, n))] ++ aux (x+1) n
      where
        createKey r s = abs $ (triangle r s) - 2000000

main :: IO ()
main = do
  let priorityQueue = fromList $ findSquares 100
  let coordinates = snd $ findMin priorityQueue
  let ans = (fst coordinates) * (snd coordinates)
  print ans  -- 2772