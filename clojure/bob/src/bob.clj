(ns bob
  (:require [clojure.string :as str]))

(defn all-upper-case? [s]
  (when (some #(Character/isLetter %) s)
    (= s (str/upper-case s))))

(defn response-for [s]
  (cond
    (str/blank? s) "Fine. Be that way!"
    (all-upper-case? s) "Whoa, chill out!"
    (str/ends-with? s "?") "Sure."
    :else "Whatever."))