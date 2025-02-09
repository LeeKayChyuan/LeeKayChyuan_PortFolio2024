{-# LANGUAGE CPP #-}
{-# LANGUAGE NoRebindableSyntax #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
{-# OPTIONS_GHC -w #-}
module Paths_assignment2 (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where


import qualified Control.Exception as Exception
import qualified Data.List as List
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude


#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir `joinFileName` name)

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath



bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath
bindir     = "C:\\Users\\USER\\Documents\\Monash\\Y2S1\\FIT2102\\33499292_LEEKAYCHYUAN\\2023Assignment2\\.stack-work\\install\\0d18834a\\bin"
libdir     = "C:\\Users\\USER\\Documents\\Monash\\Y2S1\\FIT2102\\33499292_LEEKAYCHYUAN\\2023Assignment2\\.stack-work\\install\\0d18834a\\lib\\x86_64-windows-ghc-9.2.8\\assignment2-0.1.0.0-9xS1klwTOInFjNN6j6ualy"
dynlibdir  = "C:\\Users\\USER\\Documents\\Monash\\Y2S1\\FIT2102\\33499292_LEEKAYCHYUAN\\2023Assignment2\\.stack-work\\install\\0d18834a\\lib\\x86_64-windows-ghc-9.2.8"
datadir    = "C:\\Users\\USER\\Documents\\Monash\\Y2S1\\FIT2102\\33499292_LEEKAYCHYUAN\\2023Assignment2\\.stack-work\\install\\0d18834a\\share\\x86_64-windows-ghc-9.2.8\\assignment2-0.1.0.0"
libexecdir = "C:\\Users\\USER\\Documents\\Monash\\Y2S1\\FIT2102\\33499292_LEEKAYCHYUAN\\2023Assignment2\\.stack-work\\install\\0d18834a\\libexec\\x86_64-windows-ghc-9.2.8\\assignment2-0.1.0.0"
sysconfdir = "C:\\Users\\USER\\Documents\\Monash\\Y2S1\\FIT2102\\33499292_LEEKAYCHYUAN\\2023Assignment2\\.stack-work\\install\\0d18834a\\etc"

getBinDir     = catchIO (getEnv "assignment2_bindir")     (\_ -> return bindir)
getLibDir     = catchIO (getEnv "assignment2_libdir")     (\_ -> return libdir)
getDynLibDir  = catchIO (getEnv "assignment2_dynlibdir")  (\_ -> return dynlibdir)
getDataDir    = catchIO (getEnv "assignment2_datadir")    (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "assignment2_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "assignment2_sysconfdir") (\_ -> return sysconfdir)




joinFileName :: String -> String -> FilePath
joinFileName ""  fname = fname
joinFileName "." fname = fname
joinFileName dir ""    = dir
joinFileName dir fname
  | isPathSeparator (List.last dir) = dir ++ fname
  | otherwise                       = dir ++ pathSeparator : fname

pathSeparator :: Char
pathSeparator = '\\'

isPathSeparator :: Char -> Bool
isPathSeparator c = c == '/' || c == '\\'
