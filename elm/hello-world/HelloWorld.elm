module HelloWorld exposing (..)

helloWorld : Maybe String -> String
helloWorld name =
    case name of 
        Just name ->
            "Hello, " ++ name ++ "!"
        Nothing ->
            "Hello, World!"

{-
helloWorld : Maybe String -> String
helloWorld name =
    let to = Maybe.withDefault "World" name
    in String.concat ["Hello, ", to, "!"]
-}