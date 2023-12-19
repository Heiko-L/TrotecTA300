# TrotecTA300
Serial Protocol of Trotec TA300

The device sends binary data over a serial usb converter (9600/8/n/1).
| Byte | Meaning                |
| ---- | ---------------------- |
| 0    | Header (AABB)          |
| 1    | „                      |
| 2    | Float (upper display)  |
| 3    | „                      |
| 4    | „                      |
| 5    | „                      |
| 6    | Float (lower display)  |
| 7    | „                      |
| 8    | „                      |
| 9    | „                      |
| 10   | Float velocity [m/s]   |
| 11   | „                      |
| 12   | „                      |
| 13   | „                      |
| 14   | Float temperature [°C] |
| 15   | „                      |
| 16   | „                      |
| 17   | „                      |
| 18   | Float flow [CMM]       |
| 19   | „                      |
| 20   | „                      |
| 21   | „                      |
| 22   | Float area [m²]        |
| 23   | „                      |
| 24   | „                      |
| 25   | „                      |
| 26   | displayed vel unit     |
| 27   | displayed flow unit    |
| 28   | displayed area unit    |
| 29   | displayed temp unit    |
| 30   |                        |
| 31   |                        |
| 32   |                        |
| 33   |                        |
| 34   |                        |
| 35   |                        |
| 36   |                        |
| 37   |                        |
| 38   | 16bit checksum         |
| 39   | „                      |

