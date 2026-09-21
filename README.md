# File Storage Engine
### File
Is a persistent sequence of bytes with filesystem that is stored and accessed through filesystems namespace.
### Filesystem
A system of rules and datastructures that, allow the os to be able to store, retrive, delete, update and manage peristent data and metadata

## Description
This is a system that allows storage of files, but the file size, mime type is limited to my needs and purpose of the project.

## Goals
I want a robust application that will store files, be resilient whenever a business rule fails, and simply learn through the project on how to have a file storage system.

## Architecture
        client
        

Upload Endpoint
        

File validation
MIME validation
Size validation
        

Streaming Storage
write chunk
update checksum


Persist Metadata
Mark File Available
        

Return Response


## Upload Lifecycle

## File Validation

### MIME validation
### Size validation
### Checksum generation

## Storage

## Metadata

## State Model

## Failure and Cleanup

## API

## Database Schema

## Storage Layout

## Security Considerations

## Testing

## Known Limitations

## Future Improvements

                            ©️ALPHASYSTEMSCORE