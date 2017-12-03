(def input (str ".^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^"))

(defn boolcheck [this, that] (true? (= this that)))
(defn left_center_trap_right_safe [min, char, max] 
  (and (boolcheck min "^") (boolcheck max ".") (boolcheck char "^")))
(defn center_right_trap_left_safe [min, char, max] 
  (and (boolcheck min ".") (boolcheck max "^") (boolcheck char "^")))
(defn left_only_trap [min, char, max] 
  (and (boolcheck min "^") (boolcheck max ".") (boolcheck char ".")))
(defn right_only_trap [min, char, max] 
  (and (boolcheck min ".") (boolcheck max ".") (boolcheck char "^")))

(defn trap? [min, char, max] 
  (or 
    (left_center_trap_right_safe min, char, max) 
    (center_right_trap_left_safe min, char, max) 
    (left_only_trap min, char, max) 
    (right_only_trap min, char, max)
  )
)


