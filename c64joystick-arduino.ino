#define BMASK 0x3F
#define DMASK 0xC0

byte last_state;

inline void send_state(byte state) {
	Serial.write(state);
	last_state = state;
}

inline byte get_state() {
	return (PINB & BMASK) | (PIND & DMASK);
}

void setup() {
	Serial.begin(9600);
	for (byte pin = 6; pin <= 13; pin++) {
		pinMode(pin, INPUT);
		digitalWrite(pin, HIGH); // pullup
	}
	send_state(get_state());
}

void loop() {
	byte state = get_state();
	if (state != last_state) send_state(state);
	delay(2);
}
