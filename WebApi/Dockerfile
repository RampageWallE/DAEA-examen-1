FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build

WORKDIR /app

COPY . .

RUN dotnet restore "WebApi.csproj"

RUN dotnet publish -c release -o /out

FROM mcr.microsoft.com/dotnet/aspnet:8.0

WORKDIR /app

COPY --from=build /out .

ENTRYPOINT ["dotnet", "WebApi.dll"]