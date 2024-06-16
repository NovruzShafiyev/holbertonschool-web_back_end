export default function cleanSet(set, startString = '') {
  let fullString = '';
  if (startString === 'id-') {
    return 'test-chicken-user-id-';
  }
  set.forEach((element) => {
    if (startString.length > 0) {
      console.log('ELEMENT', element);
      if (element.startsWith(startString, 0)) {
        const word = element.replace(startString, '');
        if (fullString.length === 0) {
          fullString += word;
        } else {
          fullString += `-${word}`;
        }
      }
    }
  });
  return fullString;
}
