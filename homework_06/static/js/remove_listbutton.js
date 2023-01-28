const dropdownButton = document.getElementById('custom-dropdown-button');
const optionsList = document.getElementById('custom-dropdown-options-list');
const placeholderOption = document.getElementById('placeholder-option');
const removeButton = document.getElementById('remove-btn');

const options = Array.from(document.getElementsByClassName('custom-dropdown__list-option'));
options.shift(); // ignore the placeholder option

const openDropdown = () => {
  optionsList.classList.add('-expanded');
  dropdownButton.setAttribute('aria-expanded', true);
  getSelectedOption().focus();
};

const toggleDropdown = (event) => {
  event.preventDefault();
  
  optionsList.classList.toggle('-expanded');
  const ariaExpanded = dropdownButton.getAttribute('aria-expanded');
  dropdownButton.setAttribute('aria-expanded', !ariaExpanded);
  
  if (optionsList.classList.contains('-expanded')) {
    getSelectedOption().focus();
  }
};

const closeDropdown = () => {
  optionsList.classList.remove('-expanded');
  dropdownButton.setAttribute('aria-expanded', false);
  dropdownButton.focus();
};

const showDeleteButton = () => {
  if (removeButton.classList.contains('dn')) {
    removeButton.classList.remove('dn')
  }
};

const processDeleteButton = () => {
  removeButton.getAttribute('selectedid')
};
 
const selectOption = (event) => {
  event.preventDefault();
  
  getSelectedOption().setAttribute('aria-selected', false);
  event.target.setAttribute('aria-selected', true);
  event.target.setAttribute('tabIndex', 0);  
  dropdownButton.textContent = event.target.textContent.trim();
  showDeleteButton();

  var choosen_id = getSelectedOption().getAttribute('userid')
  var basedhref = removeButton.getAttribute('basedhref')

  removeButton.href = basedhref+choosen_id
  removeButton.setAttribute('selectedid',choosen_id)
  removeButton.text="Remove user #"+choosen_id
  closeDropdown();
};

const getSelectedOption = () => {
  const selectedOption = options.find((option) => {
    return option.getAttribute('aria-selected') === 'true';
  });
  
  return selectedOption ? selectedOption : options[0];
};

const focusOnPreviousOption = () => {
  const position = options.indexOf(document.activeElement);
  const previousOption = options[position - 1];
  if (previousOption) {
    document.activeElement.setAttribute('tabIndex', -1);
    previousOption.setAttribute('tabIndex', 0);
    previousOption.focus();
  }
};

const focusOnNextOption = () => {
  const nextOption = document.activeElement.nextElementSibling;
  if (nextOption) {
    document.activeElement.setAttribute('tabIndex', -1);
    nextOption.setAttribute('tabIndex', 0);
    nextOption.focus();
  }
};

const focusOnFirstOption = () => {
  document.activeElement.setAttribute('tabIndex', -1);
  options[0].setAttribute('tabIndex', 0);
  options[0].focus();
};

const focusOnLastOption = () => {
  document.activeElement.setAttribute('tabIndex', -1);
  
  const lastIndex = options.length - 1;
  options[lastIndex].setAttribute('tabIndex', 0);
  options[lastIndex].focus();
};

const focusOnClosest = (event) => {
  const closestOption = options.find((option) => {
    const textContent = option.textContent.trim().toLowerCase();
    return textContent.startsWith(event.key);
  });

  if (closestOption) {
    document.activeElement.setAttribute('tabIndex', -1);
    closestOption.setAttribute('tabIndex', 0);
    closestOption.focus();
  }
};

// IE11 and Edge don't correctly support KeyboardEvent.key yet
const ENTER = { keyName: 'Enter', keyCode: 13 };
const SPACE = { keyName: 'Space', keyCode: 32 };
const ESCAPE = { keyName: 'Escape', keyCode: 27 };
const ARROW_UP = { keyName: 'ArrowUp', keyCode: 38 };
const ARROW_DOWN = { keyName: 'ArrowDown', keyCode: 40 };
const HOME = { keyName: 'Home', keyCode: 36 };
const END = { keyName: 'End', keyCode: 35 };
const PAGEUP = { keyName: 'PageUp', keyCode: 33 };
const PAGEDOWN = { keyName: 'PageDown', keyCode: 34 };
const ALPHANUMERIC = { keyName: /^[a-z0-9]$/, keyCode: /^4[8-9]|5[0-7]|6[5-9]|[7-8][0-9]|90$/ };

const handleKey = (key, eventHandler) => {
  return (event) => {
    event.preventDefault();
    
    const regexKey = new RegExp(key.keyName);
    const regexKeyCode = new RegExp(key.keyCode);
    
    if (regexKey.test(event.key) || regexKeyCode.test(event.keyCode)) {
      eventHandler(event);
    }
  }
};

// ***** Registering event listeners *****
dropdownButton.addEventListener('click', toggleDropdown);
// removeButton.addEventListener('click', toggleDropdown);
dropdownButton.addEventListener('keydown', handleKey(ENTER, toggleDropdown));
dropdownButton.addEventListener('keydown', handleKey(SPACE, toggleDropdown));
dropdownButton.addEventListener('keydown', handleKey(ARROW_UP, openDropdown));
dropdownButton.addEventListener('keydown', handleKey(ARROW_DOWN, openDropdown));

document.body.addEventListener('keyup', handleKey(ESCAPE, closeDropdown));
document.body.addEventListener('click', (event) => {
  const forbiddenTargets = [
    dropdownButton,
    placeholderOption
  ];
  
  if (!forbiddenTargets.includes(event.target)) {
    closeDropdown();
  }
}, true);

options.forEach((option) => {
  option.addEventListener('click', selectOption);  
  option.addEventListener('keypress', handleKey(ALPHANUMERIC, focusOnClosest));
  option.addEventListener('keypress', handleKey(SPACE, selectOption));
  option.addEventListener('keypress', handleKey(ENTER, selectOption));
  option.addEventListener('keyup', handleKey(ARROW_DOWN, focusOnNextOption));
  option.addEventListener('keyup', handleKey(ARROW_UP, focusOnPreviousOption));
  option.addEventListener('keyup', handleKey(HOME, focusOnFirstOption));
  option.addEventListener('keyup', handleKey(END, focusOnLastOption));
});
