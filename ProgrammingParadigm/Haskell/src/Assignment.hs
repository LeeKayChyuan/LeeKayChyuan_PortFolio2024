{-# OPTIONS_GHC -Wno-missing-export-lists #-}
--This module contains the skeleton code for the assignment.
--
-- Please do not change the names of the parseExerciseX functions, as they
-- are used by the test suite.
--
-- You may, and are highly encouraged, to create your functions.
module Assignment where

import Instances
import Parser
import Control.Applicative
import Data.List ( intercalate )

-- Main ADT
data ADT = LOperator ADTOperator ADT ADT
          | LTernary ADT ADT ADT
          | LInteger Int
          | LString String
          | LArray [ADT]
          | LTrue
          | LFalse
          | LNull
          | LEmpty
          | LNot ADT
          | LBrkt [ADT]
          | LExer2 ADTcommand
          | LFunctionalCall ADTFunctionCall
  deriving Eq

instance Show ADT where
  show (LOperator op l r) = "( " ++ show l ++ show op ++ show r ++ " )"
  show (LInteger n) = show n
  show (LString s) = s
  show (LArray xs) = "[" ++ intercalate ", " (map show xs) ++ "]" -- add , in between
  show LTrue = "true"
  show LFalse = "false"
  show LNull = "null"
  show LEmpty = ""
  show (LTernary condition trueBranch falseBranch) =
    "(" ++ show condition ++ " ? " ++ show trueBranch ++ " : " ++ show falseBranch ++ ")"
  show (LNot val) = "(!" ++ show val ++ ")"
  show (LBrkt val) = "(" ++ intercalate ", " (map show val) ++ ")" -- add , in between
  show (LExer2 val) = show val
  show (LFunctionalCall val) = show val

-- Combine Parser in all exercise
parseAllExercise :: Parser ADT
parseAllExercise = parseExerciseA <|> parseExerciseB <|> parseExerciseC

-- | EXERCISE A PART 1 : BASIC PARSER
-- Parser for integer
exerAInteger :: Parser ADT
exerAInteger = LInteger <$> int

-- Parser for string
exerAString :: Parser ADT
exerAString = do
  _ <- charTok '"'
  _ <- spaces
  content <- many (noneof "\"") -- check there is no \" inside
  _ <- spaces
  _ <- charTok '"'
  pure (LString content)

-- Parser for boolean
exerABool :: Parser ADT
exerABool = exerATrue <|> exerAFalse

exerATrue :: Parser ADT
exerATrue = LTrue <$ stringTok "true"
exerAFalse :: Parser ADT
exerAFalse = LFalse <$ stringTok "false"

-- Parser for Null
exerANull :: Parser ADT
exerANull = LNull <$ stringTok "null"

-- Parser for List
exerAArray :: Parser ADT
exerAArray = LArray <$> (charTok '[' *> (exerAValue `sepBy` commaTok) <* charTok ']') -- check value seperate by ,

sepBy1 :: Parser a -> Parser b -> Parser [a]
sepBy1 p sep = liftA2 (:) p (many (sep *> p))

sepBy :: Parser a -> Parser b -> Parser [a]
sepBy p sep= sepBy1 p sep <|> pure []

-- Combine basic parser
exerAValue :: Parser ADT
exerAValue = exerAInteger <|> exerAString <|> exerABool <|> exerANull <|> exerAArray <|> exerANot

-- | EXERCISE A PART 2 : OPERATOR
-- Data for all Operator (Logical, Arithmetic and Comparison)
data ADTOperator = And
              | Or
              | Add
              | Sub
              | Mul
              | Div
              | Exp
              | Equal
              | NotEqual
              | GreaterThan
              | LesserThan
              | LesserThanOREqual
              | GreaterThanOREqual
  deriving Eq

instance Show ADTOperator where
  show And = " && "
  show Or = " || "
  show Add = " + "
  show Sub = " - "
  show Mul = " * "
  show Div = " / "
  show Exp = " ** "
  show Equal = " === "
  show NotEqual = " !== "
  show GreaterThan = " > "
  show LesserThan = " < "
  show LesserThanOREqual = " <= "
  show GreaterThanOREqual = " >= "

-- * PARSER FOR LOGICAL
-- Parser for &&
exerAAnd :: Parser ADTOperator
exerAAnd = stringTok "&&" >> pure And

-- Parser for ||
exerAOr :: Parser ADTOperator
exerAOr = stringTok "||" >> pure Or

-- Parser for !
exerANot :: Parser ADT --in ADT data type 
exerANot = do
  _ <- charTok '('
  _ <- spaces
  _ <- charTok '!'
  _ <- spaces
  value <- exerAValue
  _ <- spaces
  _ <- charTok ')'
  pure (LNot value)

-- Combine Logical's parser
exerALogical :: Parser ADTOperator
exerALogical = exerAAnd <|> exerAOr


-- * PARSER FOR ARITHMETIC
-- Parser for +
exerAAdd :: Parser ADTOperator
exerAAdd = is '+' >> pure Add

-- Parser for -
exerASubtract :: Parser ADTOperator
exerASubtract = is '-' >> pure Sub

-- Parser for *
exerAMultiply :: Parser ADTOperator
exerAMultiply = is '*' >> pure Mul

-- Parser for /
exerADivide :: Parser ADTOperator
exerADivide = is '/' >> pure Div

-- Parser for **
exerAExponent :: Parser ADTOperator
exerAExponent = stringTok "**" >> pure Exp

-- Combine Arithmetic's parser
exerAArithmetic :: Parser ADTOperator
exerAArithmetic = exerAExponent <|> exerAAdd <|> exerASubtract <|> exerAMultiply <|> exerADivide


-- * PARSER FOR COMPARISON
-- Parser for ===
exerAEquals :: Parser ADTOperator
exerAEquals = stringTok "===" >> pure Equal

-- Parser for !==
exerANotEquals :: Parser ADTOperator
exerANotEquals = stringTok "!==" >> pure NotEqual

-- Parser for >
exerAGreaterThan :: Parser ADTOperator
exerAGreaterThan = charTok '>' >> pure GreaterThan

-- Parser for <
exerALesserThan :: Parser ADTOperator
exerALesserThan = charTok '<' >> pure LesserThan

-- Parser for <=
exerALesserThanOREqual :: Parser ADTOperator
exerALesserThanOREqual = stringTok "<=" >> pure LesserThanOREqual

-- Parser for >=
exerAGreaterThanOREqual :: Parser ADTOperator
exerAGreaterThanOREqual = stringTok ">=" >> pure GreaterThanOREqual

-- Combine Comparison's parser
exerAComparison :: Parser ADTOperator
exerAComparison = exerAEquals <|> exerANotEquals <|> exerALesserThanOREqual <|> exerAGreaterThanOREqual <|> exerAGreaterThan <|> exerALesserThan

-- Combine all Operator's Parser
exerAOperation :: Parser ADTOperator
exerAOperation = exerAComparison <|> exerALogical <|> exerAArithmetic

-- Parser to get string/char without any in between condition a-z, 0-9
exerAdata :: Parser ADT
exerAdata = do
  _ <- many (charTok ' ')
  val <- many (oneof "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
  pure (LString val)

-- Parser to parser operation properly
exerAOperationExpr :: Parser ADT
exerAOperationExpr = do
  _ <- many (charTok ' ')
  _ <- charTok '('
  _ <- spaces
  l <- parseExerciseC <|> parseExerciseA <|> exerAOperationExpr
  _ <- spaces
  operator <- exerAOperation
  _ <- spaces
  r <- parseExerciseC <|> parseExerciseA <|> exerAOperationExpr
  _ <- spaces
  _ <- charTok ')'
  pure (LOperator operator l r )

-- Parser to get data in between ( )
exerALogicExpr :: Parser ADT
exerALogicExpr = do
  _ <- charTok '('
  _ <- spaces
  value <- parseExerciseA `sepBy` commaTok -- check if it is seperated by ,
  _ <- spaces
  _ <- charTok ')'
  pure (LBrkt value)

-- | EXERCISE A PART 3 : Ternary
-- Parser for ternary
exerATernary :: Parser ADT
exerATernary = do
  _ <- charTok '('
  logic <- parseExerciseA
  _ <- spaces
  _ <- charTok '?'
  _ <- spaces
  ifTrue <- parseExerciseA
  _ <- spaces
  _ <- charTok ':'
  _ <- spaces
  ifFalse <- parseExerciseA
  _ <- charTok ')'
  pure (LTernary logic ifTrue ifFalse)

-- Parser for Empty value in ADT
adtEmpty :: Parser ADT
adtEmpty = pure LEmpty

-- Parser for ExerciseA
parseExerciseA :: Parser ADT
parseExerciseA = exerATernary <|> exerAOperationExpr <|> exerAValue <|> exerALogicExpr <|> exerAdata

-- Pretty printing functions for all Exercise, all printing is declared in here
prettyPrintExerciseA :: ADT -> String
prettyPrintExerciseA (LOperator op l r) = "( " ++ prettyPrintExerciseA l ++ show op ++ prettyPrintExerciseA r ++ " )"
prettyPrintExerciseA (LInteger n) = show n
prettyPrintExerciseA (LString s) = s
prettyPrintExerciseA (LArray xs) = "[" ++ intercalate ", " (map prettyPrintExerciseA xs) ++ "]" -- add , in between
prettyPrintExerciseA LTrue = "true"
prettyPrintExerciseA LFalse = "false"
prettyPrintExerciseA LNull = "null"
prettyPrintExerciseA LEmpty = "empty"
prettyPrintExerciseA (LTernary condition trueBranch falseBranch) =
  "(" ++ prettyPrintExerciseA condition ++ " ? " ++
  prettyPrintExerciseA trueBranch ++ " : " ++
  prettyPrintExerciseA falseBranch ++ ")"
prettyPrintExerciseA (LNot val) = "(!" ++ prettyPrintExerciseA val ++ ")"
prettyPrintExerciseA (LBrkt val) = "(" ++ intercalate ", " (map prettyPrintExerciseA val) ++ ")" -- add , in between
prettyPrintExerciseA (LExer2 val) = show val
prettyPrintExerciseA (LFunctionalCall val) = show val

-- ADT for Command
data ADTcommand = Lconst
                | LIf
                | LElse
                | Lvariable ADT ADT
                | Lvariable' ADTcommand ADTcommand
                | LBlocks ADTcommand
                | LBlocks'' ADTcommand ADT
                | LCond ADT ADTcommand
                | LCond' ADTcommand ADTcommand
                | Lempty
  deriving (Eq)

instance Show ADTcommand where
  show Lconst = "const "
  show LIf = "if"
  show LElse = " else "
  show (Lvariable var eq) = show Lconst ++ show var ++ " = " ++ show eq ++ "; "
  show (Lvariable' expr1 expr2) = show expr1 ++ show expr2
  show (LBlocks val) = "{" ++ show val ++ "}"
  show (LBlocks'' expr1 expr2) = "{" ++ show expr1 ++ show expr2 ++ "}"
  show (LCond cond t) = show LIf ++ show cond ++ show t
  show (LCond' expr1 expr2) = show expr1 ++ show LElse ++ show expr2
  show Lempty = ""

-- | EXERCISE B PART 1 : CONST DECLARATION
-- Parser for constant
exerBConstant :: Parser ADTcommand
exerBConstant = do
  _ <- many (charTok ' ')
  _ <- stringTok "const"
  _ <- spaces
  variable <- parseExerciseA
  _ <- spaces
  _ <- charTok '='
  _ <- spaces
  expr <- parseAllExercise
  _ <- spaces
  _ <- charTok ';'
  pure (Lvariable variable expr)

-- Parser for 2 or more constant 
exerBConstant' :: Parser ADTcommand
exerBConstant' = do
  initial <- exerBConstant
  _ <- spaces
  Lvariable' initial <$> exerBConstants

-- Combine all CONST's parser
exerBConstants :: Parser ADTcommand
exerBConstants = exerBConstant' <|> exerBConstant


-- | EXERCISE B PART 2 : PARSING BLOCK
-- Parser for block
exerBBlock :: Parser ADTcommand
exerBBlock = do
  _ <- many (charTok ' ')
  _ <- charTok '{'
  _ <- many (charTok ' ')
  var <- exerBConstants <|> exerBConditionals
  _ <- spaces
  _ <- charTok '}'
  pure (LBlocks var)

-- Parser for nested block
exerBBlock'' :: Parser ADTcommand
exerBBlock'' = do
  _ <- many (charTok ' ')
  _ <- charTok '{'
  _ <- many (charTok ' ')
  expr1 <- exerBConstants <|> exerBConditionals
  _ <- spaces
  val <- parseAllExercise
  _ <- charTok '}'
  pure (LBlocks'' expr1 val)

-- Parser for empty value block
exerBBlock' :: Parser ADTcommand
exerBBlock' = do
  _ <- many (charTok ' ')
  _ <- charTok '{'
  _ <- spaces
  _ <- charTok '}'
  pure (LBlocks Lempty)

-- Combine all block's parser
exerBBlocks :: Parser ADTcommand
exerBBlocks = exerBBlock'' <|> exerBBlock <|> exerBBlock'


-- | EXERCISE B PART 3 : PARSING CONDITIONAL STURCTURE
-- Parser for if (cond) {logic}
exerBConditional :: Parser ADTcommand
exerBConditional = do
  _ <- many (charTok ' ' )
  _ <- stringTok "if"
  _ <- spaces
  cond <- parseExerciseA
  _ <- spaces
  LCond cond <$> exerBBlocks

-- Parser for if (cond) {logic} else (cond) {logic}
exerBConditional' :: Parser ADTcommand
exerBConditional' = do
  _ <- many (charTok ' ')
  exer1 <- exerBConditional
  _ <- spaces
  _ <- stringTok "else"
  LCond' exer1 <$> exerBBlocks

-- Combine all Conditional's parser
exerBConditionals :: Parser ADTcommand
exerBConditionals = exerBConditional' <|> exerBConditional

-- Combine all Parsing Block's parser
parseExerciseB :: Parser ADT
parseExerciseB = do
  val <- exerBConstants <|> exerBBlocks <|> exerBConditionals
  pure (LExer2 val)

-- Pretty Print Exercise B
prettyPrintExerciseB :: ADT -> String
prettyPrintExerciseB = prettyPrintExerciseA -- exerything is declared in prettyPrintExcerciseA

-- ADT for TAIL CALL OPTIMIZATION
data ADTFunctionCall = LFunctionCall ADT ADT String
                      | LFunction
                      | LReturn ADT
                      | LFunctionStruct ADTFunctionCall ADT
                      | LFunctionStruct' ADTFunctionCall ADT ADTFunctionCall
  deriving (Eq)

instance Show ADTFunctionCall where
  show (LFunctionCall name arg end) = show name ++ show arg ++ end
  show LFunction = "function "
  show (LReturn val) = " return " ++ show val 
  show (LFunctionStruct arg logic1) = show LFunction ++ show arg ++ "{" ++ show logic1 ++ "}"
  show (LFunctionStruct' arg logic1 logic2) = show LFunction ++ show arg ++ "{" ++ show logic1 ++ show logic2 ++ "}"

-- | EXERCISE C PART 1 : FUCTION CALLS
-- Parser for function calls a( ); 
exerCfunctionCall :: Parser ADTFunctionCall
exerCfunctionCall = do
  name <- parseExerciseA
  _ <- spaces
  params <- parseExerciseA
  _ <- spaces
  end <- stringTok ";" <|> pure "" -- with or without ; is allowed
  _ <- spaces
  pure (LFunctionCall name params end)

-- | EXERCISE C PART 2 : FUNCTION STRUCTURES
-- Parser for function structures without RETURN statement
exerCfunctionStruc :: Parser ADTFunctionCall
exerCfunctionStruc = do
  _ <- stringTok "function"
  _ <- spaces
  arg <- exerCfunctionCall
  _ <- spaces
  _ <- charTok '{'
  _ <- spaces
  val <- parseExerciseB
  _ <- charTok '}'
  pure (LFunctionStruct arg val)

-- Parser for function structures without RETURN statement
exerCfunctionStruc' :: Parser ADTFunctionCall
exerCfunctionStruc' = do
  _ <- stringTok "function"
  _ <- spaces
  arg <- exerCfunctionCall
  _ <- spaces
  _ <- charTok '{'
  _ <- spaces
  val <- parseExerciseB
  _ <- spaces
  val2 <- exerCReturn
  _ <- charTok '}'
  pure (LFunctionStruct' arg val val2)

-- Parser for RETURN statement
exerCReturn :: Parser ADTFunctionCall
exerCReturn = do
  _ <- many (charTok ' ')
  _ <- stringTok "return"
  _ <- spaces
  val <- parseExerciseA <|> parseExerciseC
  pure(LReturn val)

-- Combine Function call and Function Structure's parser
parseFunctionalCall :: Parser ADT
parseFunctionalCall = do
  val <- exerCfunctionStruc' <|> exerCfunctionStruc <|> exerCReturn <|> exerCfunctionCall 
  pure (LFunctionalCall val)
  
-- This function should determine if the given code is a tail recursive function
isTailRecursive :: String -> Bool
isTailRecursive _ = False

-- Parser to print const function
parseExerciseC :: Parser ADT
parseExerciseC = parseExerciseB <|> parseFunctionalCall

-- Pretty Print Exercise C
prettyPrintExerciseC :: ADT -> String
prettyPrintExerciseC = prettyPrintExerciseA