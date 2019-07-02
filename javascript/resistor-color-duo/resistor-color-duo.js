//
// This is only a SKELETON file for the 'Resistor Color Duo' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const value = (colors) => {
  const [c1, c2] = colors;
  const strCode = `${COLORS[c1.toLowerCase()]}${COLORS[c2.toLowerCase()]}`;
  const code = parseInt(strCode);
  
  return code;
};

export const COLORS = {
  "black": 0,
  "brown": 1,
  "red": 2,
  "orange": 3,
  "yellow": 4,
  "green": 5,
  "blue": 6,
  "violet": 7,
  "grey": 8,
  "white": 9
};