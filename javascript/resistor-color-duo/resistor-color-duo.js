export const decodedValue = (colors) => {
  const colorNumbers = new Map([
    ["black", "0"],
    ["brown", "1"],
    ["red", "2"],
    ["orange", "3"],
    ["yellow", "4"],
    ["green", "5"],
    ["blue", "6"],
    ["violet", "7"],
    ["grey", "8"],
    ["white", "9"],
  ]);

  return parseInt(`${colorNumbers.get(colors[0])}${colorNumbers.get(colors[1])}`);

  /*
    return parseInt(colors.reduce((acc, val) => {
      return acc.concat(colorNumbers.get(val))
    }, ""));
   */
};
